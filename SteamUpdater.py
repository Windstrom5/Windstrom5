const { createCanvas, loadImage } = require("canvas");
const fs = require("fs");

async function generateImage(recentGames) {
  const canvasWidth = 800;
  const canvasHeight = 600;
  const padding = 20;
  const rowHeight = 40;

  const canvas = createCanvas(canvasWidth, canvasHeight);
  const ctx = canvas.getContext("2d");

  // Clear canvas
  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  // Set font properties
  const fontSize = 20;
  ctx.font = `${fontSize}px Arial`;
  ctx.fillStyle = "#000";

  // Draw table header
  const headerHeight = rowHeight;
  ctx.fillRect(padding, padding, canvasWidth - 2 * padding, headerHeight);
  ctx.fillStyle = "#FFF";
  ctx.fillText("Game Name", padding + 10, padding + headerHeight / 2);
  ctx.fillText("Playtime", canvasWidth - padding - 100, padding + headerHeight / 2);

  // Draw table rows
  const numRows = recentGames.length;
  for (let i = 0; i < numRows; i++) {
    const y = padding + headerHeight + (i * rowHeight);
    ctx.fillStyle = i % 2 === 0 ? "#EEE" : "#FFF";
    ctx.fillRect(padding, y, canvasWidth - 2 * padding, rowHeight);
    ctx.fillStyle = "#000";
    ctx.fillText(recentGames[i], padding + 10, y + rowHeight / 2);
  }

  // Save canvas to a PNG file
  const out = fs.createWriteStream(__dirname + "/generated-steam.png");
  const stream = canvas.createPNGStream();
  stream.pipe(out);
  out.on("finish", () => console.log("Image saved as generated-image.png"));
}

// Usage example with async/await
async function main() {
  try {
    // Replace steamID with the actual Steam ID
    const recentGames = await getRecentGames(76561198881808539, true);
    await generateImage(recentGames);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

main();
