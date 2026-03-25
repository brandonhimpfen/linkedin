#!/usr/bin/env node

import fs from "node:fs";

function readInput() {
  const file = process.argv[2];

  if (file) {
    return fs.readFileSync(file, "utf8");
  }

  return fs.readFileSync(0, "utf8");
}

function summarize(text) {
  const trimmed = text.trim();
  const characters = trimmed.length;
  const words = trimmed ? trimmed.split(/\s+/).length : 0;
  const paragraphs = trimmed ? trimmed.split(/\n\s*\n/).length : 0;

  return { characters, words, paragraphs };
}

try {
  const text = readInput();
  const summary = summarize(text);

  console.log(JSON.stringify(summary, null, 2));
} catch (error) {
  console.error(`Failed to read input: ${error.message}`);
  process.exit(1);
}
