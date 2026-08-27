function openingSection(body: string): string {
  const lines = body.split("\n");
  const end = lines.findIndex((line) => /^---\s*$/.test(line) || /^##\s+/.test(line));
  const section = lines.slice(0, end === -1 ? lines.length : end).join("\n").trim();
  if (!section) throw new Error("newsletter body has no opening section for the kind:1 announcement");
  return section;
}

function cleanOpeningProse(section: string): string {
  const paragraphs = section
    .split(/\n\s*\n/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);

  if (/^Welcome back to Nostr Compass\b/i.test(paragraphs[0] ?? "")) {
    paragraphs.shift();
  }

  if (paragraphs.length === 0) {
    throw new Error("newsletter opening section contains only the generic welcome line");
  }

  paragraphs[0] = paragraphs[0].replace(/^\*\*This week:\*\*\s*/i, "");

  return paragraphs
    .map((paragraph) =>
      paragraph
        .replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1")
        .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
        .replace(/\*\*([^*]+)\*\*/g, "$1"),
    )
    .join("\n\n")
    .trim();
}

export function buildAnnouncementContent(title: string, body: string, naddr: string): string {
  const prose = cleanOpeningProse(openingSection(body));
  return [
    `${title} is out. Here is what changed across Nostr this week:`,
    prose,
    `Read the full issue: nostr:${naddr}`,
  ].join("\n\n");
}
