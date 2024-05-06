import fs from "fs";
import axios from "axios";
import { createCanvas, loadImage } from "canvas";
import { configDotenv } from "dotenv";

configDotenv();

(async () => {
  // Fetch data from Discord's Recent Games API
  const response = await axios.get(
    "https://discord.com/api/v9/users/333017995368464385/profile/recent-games",
    headers: {
        Authorization: `${process.env.DC_KEY}`, // Replace 'DISCORD_BOT_TOKEN' with the name of your Discord bot token environment variable
      },
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

  games.forEach(async (game, index) => {
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
        const filePath = "generated-discord.png";
        // Check if the file exists
        fs.access(filePath, fs.constants.F_OK, (err) => {
          if (!err) {
            // If the file exists, unlink (delete) it
            fs.unlinkSync(filePath);
          }
          // Write the new image file
          fs.writeFile(filePath, buffer, (writeErr) => {
            if (writeErr) {
              console.error("Error writing image file:", writeErr);
            } else {
              console.log(`Image saved successfully at ${filePath}`);
            }
          });
        });
      })
      .catch((error) => {
        console.error("Error loading image:", error);
      });
  });
})();
