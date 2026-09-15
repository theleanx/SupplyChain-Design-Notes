#!/usr/bin/env node
// Render Module 3 SVGs at full and narrow widths, then build review contact sheets.

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { createRequire } from "node:module";

const runtimeModules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
const require = createRequire(runtimeModules ? path.join(runtimeModules, "entry.cjs") : import.meta.url);
const sharp = require("sharp");

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const source = path.join(root, "assets", "diagrams", "module-3");
const output = process.env.MODULE3_QA_OUTPUT || "/tmp/module3-visual-qa";

async function svgFiles(directory) {
  const files = [];
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const candidate = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await svgFiles(candidate));
    if (entry.isFile() && entry.name.endsWith(".svg")) files.push(candidate);
  }
  return files.sort();
}

async function renderAll(files, name, width, height) {
  const directory = path.join(output, name);
  await fs.mkdir(directory, { recursive: true });
  const rendered = [];
  for (const file of files) {
    const relative = path.relative(source, file).replaceAll(path.sep, "-").replace(/\.svg$/, ".png");
    const target = path.join(directory, relative);
    await sharp(file).resize(width, height, { fit: "fill" }).png().toFile(target);
    rendered.push(target);
  }
  return rendered;
}

async function contactSheet(files, name, thumbWidth, thumbHeight) {
  const columns = 5;
  const rows = Math.ceil(files.length / columns);
  const composites = [];
  for (let index = 0; index < files.length; index += 1) {
    const input = await sharp(files[index]).resize(thumbWidth, thumbHeight).png().toBuffer();
    composites.push({
      input,
      left: (index % columns) * thumbWidth,
      top: Math.floor(index / columns) * thumbHeight,
    });
  }
  const target = path.join(output, `${name}-contact-sheet.png`);
  await sharp({
    create: {
      width: columns * thumbWidth,
      height: rows * thumbHeight,
      channels: 4,
      background: "#ffffff",
    },
  }).composite(composites).png().toFile(target);
  return target;
}

await fs.rm(output, { recursive: true, force: true });
const files = await svgFiles(source);
if (files.length !== 35) throw new Error(`Expected 35 Module 3 SVGs, found ${files.length}`);

const full = await renderAll(files, "full", 1160, 696);
const narrow = await renderAll(files, "narrow", 448, 269);
const fullSheet = await contactSheet(full, "full", 290, 174);
const narrowSheet = await contactSheet(narrow, "narrow", 224, 135);
console.log(`Rendered ${files.length} SVGs at full and narrow widths.`);
console.log(fullSheet);
console.log(narrowSheet);
