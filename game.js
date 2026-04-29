<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>NEON RUNNER PRO</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root { --cyan: #00f5ff; --magenta: #ff00c8; --bg: #000; }
        * { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }
        body { width:100%; height:100vh; background:#000; display:flex; align-items:center; justify-content:center; font-family:'Orbitron', sans-serif; overflow:hidden; }
        #shell { position:relative; width:100%; max-width:420px; height:100vh; background:var(--bg); overflow:hidden; display:flex; flex-direction:column; border: 1px solid #222; }
        .screen { position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:100; background: rgba(0,0,0,0.9); transition: 0.3s; }
        .hidden { opacity:0; pointer-events:none; }
        .btn-primary { width:240px; padding:16px; background: linear-gradient(135deg, var(--cyan), var(--magenta)); border:none; border-radius:8px; font-family:'Orbitron'; font-size:18px; font-weight:900; color:#000; cursor:pointer; margin:10px 0; }
        #hud { position:absolute; top:0; left:0; right:0; padding:20px; display:flex; justify-content:space-between; pointer-events:none; z-index:10; }
        .score-text { color: var(--cyan); font-size: 24px; font-weight: 900; }
        canvas { display: block; width: 100%; height: 100%; }
        .shake { animation: shake 0.2s ease-in-out; }
        @keyframes shake { 0%, 100% { transform:translate(0,0); } 25% { transform:translate(-5px,5px); } 50% { transform:translate(5px,-5px); } }
    </style>
</head>
<body>
    <div id="shell">
        <div class="screen" id="homeScreen">
            <h1 style="color:#fff; font-size:40px; text-shadow: 0 0 15px var(--cyan);">NEON RUNNER</h1>
            <button class="btn-primary" onclick="startGame()">START</button>
        </div>
        <div id="gameArea" style="flex:1; position:relative; display:none;">
            <div id="hud">
                <div class="score-text" id="hudScore">0</div>
                <div id="hudLives" style="font-size:20px; color:#fff;">❤️❤️❤️</div>
            </div>
            <canvas id="gameCanvas"></canvas>
        </div>
        <div class="screen hidden" id="deathScreen">
            <h2 style="color:var(--magenta); font-size:32px;">GAME OVER</h2>
            <p id="finalScore" style="color:#fff; margin:20px 0;">Score: 0</p>
            <button class="btn-primary" onclick="startGame()">RETRY</button>
        </div>
    </div>
    <script src="game.js"></script>
</body>
</html>