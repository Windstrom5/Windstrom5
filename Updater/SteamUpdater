const axios = require("axios");
const fs = require("fs");
const { createCanvas, loadImage } = require("canvas");

(async () => {
  // Fetch data from Discord's Recent Games API
  const response = await axios.get(
    "https://discord.com/api/v9/users/333017995368464385/profile/recent-games",
    { headers: JSON.parse(process.env.HEADERS) }
  );
  const games = response.data.recent_games;

  // Create a canvas for generating the image
  const canvas = createCanvas(800, 800);
  const ctx = canvas.getContext("2d");

  // Draw a table with game names and logos
  const cellWidth = 200;
  const cellHeight = 200;
  const numRows = Math.ceil(games.length / 2);
  const padding = 10;

  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "black";
  ctx.font = "20px Arial";

  games.forEach((game, index) => {
    const row = Math.floor(index / 2);
    const col = index % 2;
    const x = col * (cellWidth + padding);
    const y = row * (cellHeight + padding);

    // Draw game name
    ctx.fillText(game.application.name, x + 10, y + 30);

    // Load game logo
    loadImage(`https://cdn.discordapp.com/app-icons/${game.application.id}/${game.application.icon}.png`)
      .then((logo) => {
        // Draw game logo
        ctx.drawImage(logo, x + 10, y + 50, 100, 100);

        // Save the generated image
        const buffer = canvas.toBuffer("image/png", {
          quality: 1,
          compressionLevel: 0,
        });
        fs.writeFileSync("generated-discord.png", buffer);
        console.log("Image saved successfully.");
      })
      .catch((error) => {
        console.error("Error loading image:", error);
      });
  });
})();
