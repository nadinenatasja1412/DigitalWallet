const http = require("http");

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  try {
    res.setHeader("Content-Type", "application/json");

    if (req.url === "/" && req.method === "GET") {
      res.writeHead(200);
      res.end(JSON.stringify({ message: "Welcome to the Home Page" }));
    } 
    else if (req.url === "/about" && req.method === "GET") {
      res.writeHead(200);
      res.end(JSON.stringify({ message: "About Page" }));
    } 
    else {
      res.writeHead(404);
      res.end(JSON.stringify({ error: "Not Found" }));
    }
  } catch (error) {
    res.writeHead(500);
    res.end(JSON.stringify({ error: "Internal Server Error" }));
    console.error("Server Error:", error);
  }
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
