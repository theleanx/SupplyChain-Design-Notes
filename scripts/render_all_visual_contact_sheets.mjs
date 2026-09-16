#!/usr/bin/env node
// Render every repository SVG at full and narrow widths, then build labeled contact sheets.

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { createRequire } from "node:module";

const runtimeModules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
const require = createRequire(runtimeModules ? path.join(runtimeModules, "entry.cjs") : import.meta.url);
const sharp = require("sharp");

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const diagramRoot = path.join(root, "assets", "diagrams");
const output = path.resolve(process.env.VISUAL_QA_OUTPUT || "/tmp/supply-chain-visual-qa");
const temporaryRoot = path.resolve(process.env.TMPDIR || "/tmp");
if (output !== temporaryRoot && !output.startsWith(`${temporaryRoot}${path.sep}`)) {
  throw new Error(`VISUAL_QA_OUTPUT must remain under ${temporaryRoot}`);
}
const expected = new Map([
  ["module-1", 36],
  ["module-2", 9],
  ["module-3", 35],
]);

async function svgFiles(directory) {
  const files = [];
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const candidate = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await svgFiles(candidate));
    if (entry.isFile() && entry.name.endsWith(".svg")) files.push(candidate);
  }
  return files.sort();
}

function safeName(file, source) {
  return path.relative(source, file).replaceAll(path.sep, "-").replace(/\.svg$/, ".png");
}

async function render(files, source, directory, width, height) {
  await fs.mkdir(directory, { recursive: true });
  const rendered = [];
  for (const file of files) {
    const target = path.join(directory, safeName(file, source));
    await sharp(file).resize(width, height, { fit: "fill" }).png().toFile(target);
    rendered.push({ target, label: path.relative(source, file).replaceAll(path.sep, "/") });
  }
  return rendered;
}

function labelSvg(label, width, height) {
  const escaped = label
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
  return Buffer.from(
    `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">` +
      `<rect width="100%" height="100%" fill="#f4f6f8"/>` +
      `<text x="8" y="18" font-family="Arial, sans-serif" font-size="12" fill="#1f2933">${escaped}</text>` +
    `</svg>`,
  );
}

async function contactSheet(items, target, thumbWidth, thumbHeight) {
  const columns = 4;
  const labelHeight = 28;
  const rows = Math.ceil(items.length / columns);
  const composites = [];
  for (let index = 0; index < items.length; index += 1) {
    const left = (index % columns) * thumbWidth;
    const top = Math.floor(index / columns) * (thumbHeight + labelHeight);
    const input = await sharp(items[index].target).resize(thumbWidth, thumbHeight).png().toBuffer();
    composites.push({ input, left, top });
    composites.push({ input: labelSvg(items[index].label, thumbWidth, labelHeight), left, top: top + thumbHeight });
  }
  await sharp({
    create: {
      width: columns * thumbWidth,
      height: rows * (thumbHeight + labelHeight),
      channels: 4,
      background: "#ffffff",
    },
  }).composite(composites).png().toFile(target);
}

await fs.rm(output, { recursive: true, force: true });
await fs.mkdir(output, { recursive: true });

for (const [module, expectedCount] of expected) {
  const source = path.join(diagramRoot, module);
  const files = await svgFiles(source);
  if (files.length !== expectedCount) {
    throw new Error(`Expected ${expectedCount} ${module} SVGs, found ${files.length}`);
  }
  const moduleOutput = path.join(output, module);
  const full = await render(files, source, path.join(moduleOutput, "full"), 1160, 696);
  const narrow = await render(files, source, path.join(moduleOutput, "narrow"), 448, 269);
  await contactSheet(full, path.join(output, `${module}-full-contact-sheet.png`), 290, 174);
  await contactSheet(narrow, path.join(output, `${module}-narrow-contact-sheet.png`), 224, 135);
  console.log(`Rendered ${module}: ${files.length} SVGs at full and narrow widths.`);
}

console.log(output);
