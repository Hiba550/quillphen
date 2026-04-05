
$dir = "d:\mc packs\sites\revmap\quillphen"
$BASE = "https://quillphen.netlify.app"
$AVATAR = "https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp"
$MDR_PATH = "M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"

function Write-Page {
  param(
    [string]$File,
    [string]$PageTitle,
    [string]$Desc,
    [string]$Keywords,
    [string]$Icon,
    [string]$IcColor = "",
    [string]$Name,
    [string]$Tagline,
    [string]$EdChip,
    [string]$TypChip,
    [string]$Body,
    [string]$MrUrl,
    [string]$CfUrl = ""
  )

  $slug = $File -replace "\.html$",""
  $cfBtn = ""
  if ($CfUrl) { $cfBtn = "<a href=`"$CfUrl`" target=`"_blank`" rel=`"noopener`" class=`"dl-btn s`">CurseForge</a>" }

  $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3W2T4M8K8"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-K3W2T4M8K8');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$PageTitle | QuillPhen</title>
  <meta name="description" content="$Desc">
  <meta name="keywords" content="$Keywords">
  <meta name="author" content="QuillPhen">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="$BASE/$File">
  <meta property="og:type" content="article">
  <meta property="og:url" content="$BASE/$File">
  <meta property="og:title" content="$PageTitle | QuillPhen">
  <meta property="og:description" content="$Desc">
  <meta property="og:image" content="$AVATAR">
  <meta property="og:site_name" content="QuillPhen">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="$PageTitle | QuillPhen">
  <meta name="twitter:description" content="$Desc">
  <meta name="twitter:image" content="$AVATAR">
  <meta name="theme-color" content="#006E1C">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="apple-touch-icon" href="favicon.ico">
  <link rel="manifest" href="manifest.json">
  <link rel="preload" href="styles.css" as="style">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="top-bar" id="top-bar">
  <div class="bar-inner">
    <a href="index.html" class="bar-brand">
      <div class="bar-avatar"><img src="$AVATAR" alt="QuillPhen" width="36" height="36" loading="eager"></div>
      <span class="bar-name">QuillPhen</span>
    </a>
    <nav class="bar-nav">
      <a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener" class="btn-nav">
        <svg style="width:16px;height:16px;fill:currentColor" viewBox="0 0 512 514" aria-hidden="true"><path d="$MDR_PATH"/></svg>
        <span>Modrinth</span>
      </a>
      <a href="index.html" class="btn-nav"><span>All Projects</span></a>
    </nav>
  </div>
</header>
<div class="page-wrap">
  <a href="index.html" class="back-btn"><span class="msrnd" aria-hidden="true">arrow_back</span>All Projects</a>
  <div class="proj-hero">
    <div class="proj-hero-ico $IcColor" aria-hidden="true"><span class="msrnd">$Icon</span></div>
    <h1>$Name</h1>
    <p class="sub">$Tagline</p>
    <div class="proj-hero-chips">$EdChip $TypChip</div>
  </div>
  <div class="ad-slot ad-banner" id="ad-top"><div id="container-1487dceabcc3b2d80cbac6310506ec7a"></div></div>
$Body
  <div class="dl-section">
    <h2><span class="msrnd" aria-hidden="true">download</span> Download</h2>
    <p>Free to download — get it on Modrinth to stay updated.</p>
    <div class="dl-btns">
      <a href="$MrUrl" target="_blank" rel="noopener" class="dl-btn p">
        <svg style="width:16px;height:16px;fill:currentColor" viewBox="0 0 512 514"><path d="$MDR_PATH"/></svg>
        Download on Modrinth
      </a>
      $cfBtn
    </div>
  </div>
</div>
<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <a href="index.html" class="bar-brand">
        <div class="bar-avatar"><img src="$AVATAR" alt="QuillPhen" width="36" height="36" loading="lazy"></div>
        <span class="bar-name">QuillPhen</span>
      </a>
      <p>Quality-of-life Minecraft mods, data packs, resource packs and shaders for Java &amp; Bedrock Edition.</p>
    </div>
    <div>
      <p class="footer-col-title">Links</p>
      <ul class="footer-links">
        <li><a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener">Modrinth Profile</a></li>
        <li><a href="https://www.curseforge.com/members/quillphen/projects" target="_blank" rel="noopener">CurseForge Profile</a></li>
        <li><a href="index.html">All Projects</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">More</p>
      <ul class="footer-links">
        <li><a href="sitemap.xml">Sitemap</a></li>
        <li><a href="rss.xml">RSS Feed</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 QuillPhen. Not affiliated with Mojang or Microsoft.</p>
    <div class="footer-bottom-links"><a href="robots.txt">Robots</a><a href="sitemap.xml">Sitemap</a></div>
  </div>
</footer>
<script async="async" data-cfasync="false" src="//pl26879834.profitableratecpm.com/1487dceabcc3b2d80cbac6310506ec7a/invoke.js"></script>
<script>const tb=document.getElementById('top-bar');window.addEventListener('scroll',()=>tb.classList.toggle('scrolled',window.scrollY>8),{passive:true});</script>
</body>
</html>
"@
  Set-Content -Path "$dir\$File" -Value $html -Encoding UTF8
  Write-Host "  [OK] $File"
}

# ─── PROJECT PAGES ─────────────────────────────────────────────────────────
$jChip = '<span class="chip chip-java">Java Edition</span>'
$bChip = '<span class="chip chip-bedrock">Bedrock Edition</span>'
$dpChip = '<span class="chip chip-datapack">Data Pack</span>'
$modChip = '<span class="chip chip-mod">Mod</span>'
$rpChip = '<span class="chip chip-resourcepack">Resource Pack</span>'
$shChip = '<span class="chip chip-shader">Shader</span>'
$adChip = '<span class="chip chip-addon">Addon</span>'

Write-Host "Generating pages..."

# ── 1. Tree Vein Miner ────────────────────────────────────────────────
Write-Page -File "tree-vein-miner.html" `
  -PageTitle "Tree Vein Miner – Fell Entire Trees Instantly" `
  -Desc "Tree Vein Miner is a Minecraft data pack and mod that automatically removes entire trees when you crouch and break a log. Supports all wood types, Fabric, Forge, NeoForge." `
  -Keywords "tree vein miner minecraft, fell trees datapack, minecraft tree chopper, quillphen, fabric forge neoforge, auto tree felling" `
  -Icon "forest" -IcColor "" `
  -Name "Tree Vein Miner" -Tagline "Fell entire trees instantly by sneaking and breaking a log" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/tree-vein-miner" `
  -CfUrl "" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Tree Vein Miner removes entire trees — logs and leaves — when you crouch and break any log block. No more climbing trees or leaving floating treetops. Works with all vanilla wood types and is completely server-side.</p>
    <p>Compatible with Silk Touch and Fortune enchantments. Leaves decay naturally after the trunk is removed.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Instantly fells the entire tree when you crouch-break any log</li>
      <li>Works with all vanilla wood types (oak, birch, spruce, jungle, acacia, dark oak, mangrove, bamboo, cherry)</li>
      <li>Supports Silk Touch and Fortune enchantments</li>
      <li>Leaves decay naturally after trunk removal</li>
      <li>No client-side mod required — works on all servers</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Quilt</li>
      <li>Lightweight with zero performance impact</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack / Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge, Quilt, Vanilla Data Pack</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side (no client mod needed)</td></tr>
    </table>
  </div>
'@

# ── 2. Ore Vein Miner ────────────────────────────────────────────────
Write-Page -File "ore-vein-miner.html" `
  -PageTitle "Ore Vein Miner – Mine Entire Ore Veins Instantly" `
  -Desc "Ore Vein Miner automatically mines all connected ore blocks of the same type when you break one. A lightweight server-side Minecraft data pack supporting Fabric and Forge." `
  -Keywords "ore vein miner minecraft, vein mining datapack, chain mining minecraft, quillphen, fabric forge, auto ore mining" `
  -Icon "diamond" -IcColor "teal" `
  -Name "Ore Vein Miner" -Tagline "Mine an entire ore vein with a single break" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/ore-vein-miner" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Ore Vein Miner detects connected ore blocks of the same type and mines them all in a single action when you break one. Ideal for survival and SMP play where efficient mining saves time without being overpowered.</p>
    <p>Works with all vanilla ore types including diamond, iron, coal, gold, copper, emerald, redstone, lapis, nether quartz, and ancient debris.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Automatically mines all connected same-type ore blocks</li>
      <li>Supports all vanilla ores: diamond, iron, gold, copper, emerald, redstone, lapis, coal, quartz, ancient debris</li>
      <li>Fortune and Silk Touch enchantment support</li>
      <li>Tool durability is correctly applied per block mined</li>
      <li>Server-side only — no client installation required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and as a vanilla data pack</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack / Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge, Vanilla Data Pack</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 3. VeinMiner ────────────────────────────────────────────────────
Write-Page -File "vein-miner.html" `
  -PageTitle "VeinMiner – Chain Mine Ores and Fell Trees" `
  -Desc "VeinMiner is a Minecraft data pack that lets you mine entire ore veins and fell complete trees with a single break. Lightweight, server-side, supports all loaders." `
  -Keywords "veinminer minecraft, chain mining, vein mining datapack, tree chopper minecraft, quillphen, fabric forge" `
  -Icon "hardware" -IcColor "" `
  -Name "VeinMiner" -Tagline "Mine ore veins and fell trees efficiently with chain mining" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/vein_miner" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>VeinMiner is a lightweight all-in-one data pack that combines ore vein mining and tree felling into a single, simple package. Sneak while mining to activate the chain mining behavior.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Mines entire connected ore veins in one action</li>
      <li>Fells complete trees when sneaking</li>
      <li>Fortune and Silk Touch support</li>
      <li>Handles tool durability correctly</li>
      <li>No client mod needed — pure server-side</li>
      <li>Works with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge, Quilt, Vanilla</td></tr>
      <tr><th>Minecraft</th><td>1.16 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 4. Vein Miner Preview ─────────────────────────────────────────────
Write-Page -File "vein-miner-preview.html" `
  -PageTitle "Vein Miner & Preview – Visual Vein Mining with Preview" `
  -Desc "Universal Minecraft vein miner data pack for 1.14–1.21+ with sneaking activation, Silk Touch and Fortune support, custom block lists, and visual previews in modern versions." `
  -Keywords "vein miner preview minecraft, vein mining visual, minecraft datapack, silk touch fortune vein miner, quillphen" `
  -Icon "preview" -IcColor "teal" `
  -Name "Vein Miner &amp; Preview" -Tagline "Universal vein miner with visual previews and full enchantment support" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/the-vein-miner" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>A universal vein miner data pack for Minecraft 1.14–1.21+ that lets you mine entire ore veins and trees by sneaking and breaking. This version adds visual previews of which blocks will be mined before you commit — see exactly what you are about to harvest.</p>
    <p>Supports custom block lists, Silk Touch, Fortune, durability handling, and works on multiplayer servers.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Visual preview highlights blocks that will be mined</li>
      <li>Supports Minecraft 1.14 through 1.21+</li>
      <li>Silk Touch and Fortune enchantment compatibility</li>
      <li>Custom block list support</li>
      <li>Correct tool durability deduction</li>
      <li>Multiplayer and SMP server compatible</li>
      <li>Works with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.14 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 5. Dynamic Lighting (Java datapack) ─────────────────────────────
Write-Page -File "dynamic-lighting.html" `
  -PageTitle "Dynamic Lighting – Real-Time Item Lighting for Java Edition" `
  -Desc "Dynamic Lighting is a Minecraft Java data pack that emits real-time light from held light-emitting items and glowing entities. No mods required — pure server-side." `
  -Keywords "dynamic lighting minecraft java, held item light datapack, minecraft torch lighting, quillphen, fabric forge server" `
  -Icon "flashlight_on" -IcColor "amber" `
  -Name "Dynamic Lighting" -Tagline "Real-time light from held items and glowing entities — no client mod needed" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/dynamic-lighting" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Dynamic Lighting brings real-time environmental lighting to Minecraft Java Edition without any client-side modification. When you hold a light-emitting item such as a torch, lantern, glowstone, or sea lantern, the environment around you lights up dynamically.</p>
    <p>This data pack works server-side and is compatible with vanilla clients, making it perfect for any SMP or survival server.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Dynamic light emission from held light-emitting items</li>
      <li>Supports torches, lanterns, glowstone, sea lanterns, and more</li>
      <li>Works with glowing entities (magma cubes, blazes, etc.)</li>
      <li>No client-side installation required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Vanilla servers</li>
      <li>Zero client performance impact</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge, Vanilla</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 6. Tree Veinminer Enchantment ─────────────────────────────────────
Write-Page -File "tree-veinminer-enchant.html" `
  -PageTitle "Tree Veinminer Enchantment – Axe Enchantment for Instant Tree Felling" `
  -Desc "Adds a Tree Veinminer enchantment to axes in Minecraft. Instantly fell entire trees with one swing when the enchantment is active. A Minecraft data pack for Fabric, Forge, and NeoForge." `
  -Keywords "tree veinminer enchantment minecraft, axe enchantment tree, instant tree felling, quillphen datapack, fabric forge" `
  -Icon "auto_fix_high" -IcColor "amber" `
  -Name "Tree Veinminer Enchantment" -Tagline "Enchant your axe to instantly fell entire trees in one swing" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/tree-veinminer-enchant" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>This data pack adds a custom Tree Veinminer enchantment for axes. When your axe is enchanted with Tree Veinminer, breaking any log will automatically fell the entire connected tree. No need to sneak — the enchantment handles it automatically.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>New "Tree Veinminer" enchantment for axe tools</li>
      <li>Instantly fells entire trees when enchantment is active</li>
      <li>Works with all vanilla wood types</li>
      <li>Enchantment found in enchanting table and anvil</li>
      <li>Compatible with other axe enchantments</li>
      <li>Server-side only — no client mod needed</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 7. Ore Veinminer Enchantment ──────────────────────────────────────
Write-Page -File "ore-veinminer-enchant.html" `
  -PageTitle "Ore Veinminer Enchantment – Pickaxe Enchantment for Chain Mining" `
  -Desc "Adds an Ore Veinminer enchantment for pickaxes in Minecraft. Mine entire ore veins with a single strike when the enchantment is active. Minecraft data pack for Fabric, Forge, NeoForge." `
  -Keywords "ore veinminer enchantment minecraft, pickaxe enchantment vein mining, chain mining enchantment, quillphen, fabric forge" `
  -Icon "auto_fix_high" -IcColor "teal" `
  -Name "Ore Veinminer Enchantment" -Tagline "Enchant your pickaxe to mine entire ore veins instantly" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/ore-veinminer-enchant" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Adds a custom Ore Veinminer enchantment for pickaxes. When your pickaxe is enchanted with Ore Veinminer, breaking an ore block automatically mines all connected ore blocks of the same type. Dig smarter, not harder.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>New "Ore Veinminer" enchantment for pickaxes</li>
      <li>Chains through all connected same-type ore blocks</li>
      <li>Compatible with Fortune and Silk Touch</li>
      <li>Correct tool durability per block mined</li>
      <li>Enchantment available in enchanting table and anvil</li>
      <li>Server-side only — no client mod needed</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 8. Custom Vein Miner ──────────────────────────────────────────────
Write-Page -File "custom-vein-miner.html" `
  -PageTitle "Custom Vein Miner – Fully Configurable Vein Mining Datapack" `
  -Desc "Custom Vein Miner lets you mine entire ore veins and fell whole trees in one swing with full Fortune and Silk Touch support. Highly configurable for any Minecraft server." `
  -Keywords "custom vein miner minecraft, configurable vein mining datapack, fortune silk touch vein miner, quillphen, server datapack" `
  -Icon "tune" -IcColor "" `
  -Name "Custom Vein Miner" -Tagline "Fully configurable vein mining and tree felling with enchantment support" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/custom-vm" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Custom Vein Miner gives you fine-grained control over vein mining behavior. Configure which blocks are included, the maximum vein size, sneak activation, and enchantment interactions. Full Fortune and Silk Touch support included.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Mines entire ore veins and fells whole trees</li>
      <li>Full Fortune and Silk Touch enchantment support</li>
      <li>Configurable block lists and vein size limits</li>
      <li>Sneak-to-activate mode</li>
      <li>Correct tool durability handling</li>
      <li>Server-side — no client installation</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 9. Dynamic Light Shader ───────────────────────────────────────────
Write-Page -File "dynamic-light-shader.html" `
  -PageTitle "Dynamic Light Shader – Held Item Glow for Iris and OptiFine" `
  -Desc "A simple, lightweight Minecraft shader for Iris and OptiFine that makes held light-emitting items emit visible light with a bloom glow effect. Low performance impact." `
  -Keywords "dynamic light shader minecraft, iris optifine held item light, minecraft glow shader, quillphen, low spec shader" `
  -Icon "auto_awesome" -IcColor "amber" `
  -Name "Dynamic Light Shader" -Tagline "Lightweight shader — held items emit real visible light and glow" `
  -EdChip $jChip -TypChip $shChip `
  -MrUrl "https://modrinth.com/shader/dynamic-light-shader" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>A simple baseline shader that adds a glowing light emission effect to items held in your hand. Designed to be lightweight and work on low-end hardware while providing a beautiful visual enhancement.</p>
    <p>Compatible with both Iris Shaders and OptiFine. Works alongside other shader packs.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Real glow and light bloom for held light-emitting items</li>
      <li>Low performance impact — designed for low-end PCs</li>
      <li>Compatible with Iris Shaders and OptiFine</li>
      <li>Vanilla-like aesthetic — subtle and clean</li>
      <li>No major visual changes to the rest of the world</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Shader Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Shader Loaders</th><td>Iris, OptiFine</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Performance</th><td>Low impact — suitable for all tiers</td></tr>
    </table>
  </div>
'@

# ── 10. Auto Builder ──────────────────────────────────────────────────
Write-Page -File "auto-builder.html" `
  -PageTitle "Auto Builder – Automatically Place Blocks While Walking" `
  -Desc "Auto Builder is a Minecraft data pack that automatically places blocks beneath you as you walk forward, making bridge-building and path-laying effortless on any server." `
  -Keywords "auto builder minecraft, auto bridge datapack, automatic block placement minecraft, quillphen, bridging datapack" `
  -Icon "construction" -IcColor "teal" `
  -Name "Auto Builder" -Tagline "Walk forward and blocks place themselves automatically beneath you" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/auto-bridge" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Auto Builder automatically places the block in your main hand beneath you as you walk forward. Simply hold the block you want to place and move — the data pack handles the rest. Perfect for building bridges over lava, water, or void, or creating paths quickly across large distances.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Automatically places held blocks beneath you while walking forward</li>
      <li>Works with any solid block held in main hand</li>
      <li>No configuration required — works instantly</li>
      <li>Perfect for bridges, paths, and platforms</li>
      <li>Server-side — no client mod required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 11. Mob Capture ORB ───────────────────────────────────────────────
Write-Page -File "mob-capture-orb.html" `
  -PageTitle "Mob Capture ORB – Capture and Carry Mobs in Orbs" `
  -Desc "Mob Capture ORB is a Minecraft mod that lets you capture any mob in a magical orb, carry it in your inventory, and release it anywhere you want. For Fabric and Forge." `
  -Keywords "mob capture orb minecraft, capture mob mod, pokemon ball minecraft mod, quillphen, fabric forge mob carry" `
  -Icon "catching_pokemon" -IcColor "amber" `
  -Name "Mob Capture ORB" -Tagline "Capture any mob in a magical orb and release it anywhere" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/mob-capture-orb" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Mob Capture ORB adds a magical orb item to Minecraft that can capture any living mob. Simply right-click a mob with the orb to capture it, then right-click again on the ground to release it at the desired location. The mob is safely stored in your inventory.</p>
    <p>Perfect for transporting animals, moving villagers, or relocating hostile mobs. Compatible with both friendly and hostile entities.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Capture any mob with a right-click</li>
      <li>Mob is safely stored in the orb item in your inventory</li>
      <li>Release the mob by right-clicking on any surface</li>
      <li>Works with passive, neutral, and hostile mobs</li>
      <li>Villagers, animals, and monsters all supported</li>
      <li>Compatible with Fabric and Forge</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge</td></tr>
      <tr><th>Minecraft</th><td>1.19 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client &amp; Server</td></tr>
    </table>
  </div>
'@

# ── 12. Auto Replant Crops ────────────────────────────────────────────
Write-Page -File "auto-replant-crops.html" `
  -PageTitle "Auto Replant Crops – Automatically Replant Harvested Crops" `
  -Desc "Auto Replant Crops is a Minecraft data pack that automatically replants fully grown crops after harvesting. A lightweight farming QoL mod for survival and SMP servers (1.16+)." `
  -Keywords "auto replant crops minecraft, automatic farming datapack, minecraft crop replant, quillphen, farming qol, smp server" `
  -Icon "grass" -IcColor "" `
  -Name "Auto Replant Crops" -Tagline "Harvest crops and they replant themselves automatically" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/auto-replant-crops" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Auto Replant Crops removes the tedious step of manually replanting after a harvest. When a fully grown crop is broken, the data pack automatically replants a seed in the same spot using seeds from the dropped items. Your farm stays productive automatically.</p>
    <p>Works with wheat, carrots, potatoes, beetroot, nether warts, and more. Compatible with all survival and SMP setups from Minecraft 1.16 onwards.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Auto-replanting after breaking fully grown crops</li>
      <li>Supports wheat, carrots, potatoes, beetroot, nether warts</li>
      <li>Uses dropped seed items for replanting — balanced</li>
      <li>No extra setup needed — works immediately</li>
      <li>Server-side — no client mod required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Vanilla</li>
      <li>Works on Minecraft 1.16+</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.16 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 13. Coordinates HUD ───────────────────────────────────────────────
Write-Page -File "coordinates-hud.html" `
  -PageTitle "Coordinates HUD – Advanced Customizable HUD for Minecraft" `
  -Desc "Coordinates HUD is a Minecraft mod that shows an advanced, fully customizable HUD with coordinates, biome name, compass direction, time, and more. For Fabric and Forge." `
  -Keywords "coordinates hud minecraft, minecraft coordinate display mod, biome hud mod, quillphen, fabric forge hud mod, coordinates overlay" `
  -Icon "gps_fixed" -IcColor "blue" `
  -Name "Coordinates HUD" -Tagline "Advanced coordinate display mod with a fully customizable overlay" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/coordinateshud" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Coordinates HUD provides an advanced in-game HUD overlay that shows essential navigation and world information at a glance. Display your exact X, Y, Z coordinates, current biome, compass direction, in-game time, and more — all fully customizable to your preferences.</p>
    <p>Designed to be clean and minimal while providing all the information a survival player needs. Client-side mod compatible with both single-player and server play.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Displays X, Y, Z coordinates in real time</li>
      <li>Shows current biome name</li>
      <li>Compass direction and facing indicator</li>
      <li>In-game time and day counter</li>
      <li>Fully customizable position and style</li>
      <li>Works in singleplayer and on servers</li>
      <li>Compatible with Fabric, Forge, and NeoForge</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge</td></tr>
      <tr><th>Minecraft</th><td>1.19 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── 14. Waypoints ─────────────────────────────────────────────────────
Write-Page -File "waypoints.html" `
  -PageTitle "Waypoints & Teleport – Survival Waypoint System for Minecraft" `
  -Desc "Waypoints is a lightweight Minecraft data pack that adds a survival-friendly fast travel and teleport system for singleplayer and SMP servers. Supports Java 1.21.6+." `
  -Keywords "waypoints minecraft datapack, minecraft teleport waypoints, fast travel minecraft, quillphen, smp waypoints java 1.21" `
  -Icon "place" -IcColor "pink" `
  -Name "Waypoints &amp; Teleport" -Tagline "Survival-friendly waypoints and fast travel for singleplayer and SMP" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/waypoints-teleport" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Waypoints adds a simple, survival-balanced fast travel system to your Minecraft world. Set waypoints using in-game commands and teleport between them without breaking immersion. Works in both singleplayer worlds and multiplayer SMP servers. Requires Java 1.21.6 or later.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Create, name, and manage waypoints via in-game commands</li>
      <li>Teleport to any saved waypoint instantly</li>
      <li>Survival-balanced — optional cooldown and requirements</li>
      <li>Full multiplayer and SMP server support</li>
      <li>Per-player waypoints with privacy controls</li>
      <li>No client mod required — server-side only</li>
      <li>Requires Minecraft Java 1.21.6+</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.21.6+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 15. Stackable Item ────────────────────────────────────────────────
Write-Page -File "stackable-item.html" `
  -PageTitle "Stackable Item – Make Potions, Boats, and More Stackable" `
  -Desc "Stackable Item is a Minecraft data pack that makes normally unstackable items like potions, boats, saddles, and totems stackable in your inventory. Compatible with Fabric, Forge, NeoForge." `
  -Keywords "stackable items minecraft, stackable potions datapack, inventory management minecraft, quillphen, fabric forge stackable" `
  -Icon "inventory_2" -IcColor "blue" `
  -Name "Stackable Item" -Tagline "Potions, boats, saddles, totems and more — all stackable" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/stackable-item" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Stackable Item removes the frustration of non-stackable items cluttering your inventory. Potions, boats, saddles, totems of undying, and many other previously single-slot items can now stack together, freeing up precious inventory space for survival and exploration.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Potions stack up to 16 per slot</li>
      <li>Boats, saddles, and totems now stackable</li>
      <li>Significantly reduces inventory clutter</li>
      <li>No gameplay changes beyond stacking behavior</li>
      <li>Server-side — no client mod required</li>
      <li>Works with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.18 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 16. Automatic Smelt ───────────────────────────────────────────────
Write-Page -File "automatic-smelt.html" `
  -PageTitle "Automatic Smelt – Mined Blocks Auto-Drop Their Smelted Form" `
  -Desc "Automatic Smelt is a Minecraft data pack where every block you break that can be smelted drops its smelted form automatically. Mine iron and get ingots directly — no furnace needed." `
  -Keywords "automatic smelt minecraft, auto smelt datapack, mine iron ingots directly, quillphen, smelt on mine, fabric forge" `
  -Icon "local_fire_department" -IcColor "amber" `
  -Name "Automatic Smelt" -Tagline "Mine smeltable blocks and receive their smelted output automatically" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/automatic-smelt" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Automatic Smelt replaces the drop of any block that can normally be smelted with its smelted output. Mine iron ore and receive iron ingots directly. Break sand and receive glass. Chop logs and get charcoal. No furnace, no waiting — just instant smelting as you mine.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Iron ore drops iron ingots directly</li>
      <li>Gold ore drops gold ingots</li>
      <li>Sand drops glass, gravel drops flint</li>
      <li>Logs can drop charcoal</li>
      <li>Silk Touch bypasses auto-smelt behavior</li>
      <li>Server-side — no client mod needed</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.17 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 17. Automatic Smelt Tools ─────────────────────────────────────────
Write-Page -File "automatic-smelt-tools.html" `
  -PageTitle "Automatic Smelt Tools – Tool-Based Auto Smelting in Minecraft" `
  -Desc "Automatic Smelt Tools adds craftable tools that auto-smelt blocks when mined. Equip one and every smeltable block you break drops its smelted form. For Minecraft Fabric, Forge, NeoForge." `
  -Keywords "automatic smelt tools minecraft, auto smelt pickaxe, smelting tools datapack, quillphen, fabric forge auto smelt" `
  -Icon "construction" -IcColor "amber" `
  -Name "Automatic Smelt Tools" -Tagline "Craftable tools that automatically smelt blocks as you mine them" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/automatic-smelt-tools" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Automatic Smelt Tools is a tool-based variant of Auto Smelt. Instead of applying to all mining, this data pack adds special craftable tools — auto-smelt pickaxes, shovels, and axes. Equip them and every smeltable block you break automatically drops its smelted form.</p>
    <p>This gives you flexibility: use regular tools for normal mining and equip your Auto Smelt tool when you want automatic smelting.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Craftable auto-smelt variants of pickaxe, shovel, and axe</li>
      <li>Smeltable blocks drop their output when mined with these tools</li>
      <li>Selective — only auto-smelts when using the special tool</li>
      <li>Custom crafting recipes included</li>
      <li>Server-side — no client mod required</li>
      <li>Works with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.17 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 18. Better Mob Heads ──────────────────────────────────────────────
Write-Page -File "better-mob-heads.html" `
  -PageTitle "Better Mob Heads – Decorative Head Drops for Vanilla Mobs" `
  -Desc "Better Mob Heads gives supported vanilla Minecraft mobs a decorative custom head drop when they die, perfect for decoration and collecting. A Minecraft data pack for Fabric and Forge." `
  -Keywords "better mob heads minecraft, mob head drops datapack, minecraft decorative heads, quillphen, fabric forge mob heads" `
  -Icon "face" -IcColor "" `
  -Name "Better Mob Heads" -Tagline "Vanilla mobs drop unique decorative heads when slain" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/better-mob-heads" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Better Mob Heads adds a rare head drop to vanilla mobs that normally cannot drop heads. When a supported mob is killed, there is a chance it will drop a unique decorative mob head. Use these heads to decorate your builds, collect them as trophies, or display them in your base.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Supported vanilla mobs drop unique head items</li>
      <li>Heads are decorative and can be placed on any surface</li>
      <li>Rare drop rate for balanced survival gameplay</li>
      <li>All head textures match the respective mob appearance</li>
      <li>Server-side — no client mod required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.19 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── 19. Dynamic Lighting MCPE ─────────────────────────────────────────
Write-Page -File "dynamic-lighting-mcpe.html" `
  -PageTitle "Dynamic Lighting MCPE – Real-Time Held Item Lighting for Bedrock" `
  -Desc "Dynamic Lighting MCPE is a Minecraft Bedrock Edition addon that adds real-time dynamic lighting when holding light-emitting items like torches, lanterns, and glowstone." `
  -Keywords "dynamic lighting bedrock, mcpe dynamic lighting, minecraft pe torch lighting, held item light bedrock, quillphen, bedrock addon" `
  -Icon "lightbulb" -IcColor "amber" `
  -Name "Dynamic Lighting MCPE" -Tagline "Hold a torch and light up the world around you in Bedrock Edition" `
  -EdChip $bChip -TypChip $adChip `
  -MrUrl "https://modrinth.com/user/quillphen" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Dynamic Lighting MCPE brings real-time environmental lighting to Minecraft Bedrock Edition. When you hold a torch, lantern, glowstone block, or any other light-emitting item, the area around you illuminates dynamically — just like you would expect in a modern lighting system.</p>
    <p>Enhance cave exploration and nighttime gameplay without needing to place torches everywhere.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Torches, lanterns, glowstone emit light when held</li>
      <li>Works in caves, at night, and underwater</li>
      <li>No performance impact for most devices</li>
      <li>Compatible with other Bedrock addons</li>
      <li>Easy to install — standard .mcaddon file</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Addon</td></tr>
      <tr><th>Edition</th><td>Bedrock Edition (MCPE / Console / Windows)</td></tr>
      <tr><th>Minecraft</th><td>1.18+</td></tr>
    </table>
  </div>
'@

# ─── UPDATE EXISTING PAGES ─────────────────────────────────────────────────
Write-Host "`nUpdating existing pages..."

# ── cave-vision.html (Night Vision datapack) ──────────────────────────
Write-Page -File "cave-vision.html" `
  -PageTitle "Night Vision Data Pack – Cave Exploration for Minecraft Java" `
  -Desc "Night Vision is a lightweight Minecraft Java data pack that gives all players permanent Night Vision, making cave exploration and dark areas effortlessly bright without any equipment." `
  -Keywords "night vision datapack minecraft, cave vision java, permanent night vision minecraft, quillphen, fabric forge server datapack" `
  -Icon "remove_red_eye" -IcColor "" `
  -Name "Night Vision" -Tagline "Permanent Night Vision for all players — explore caves without lighting" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/cave-vision" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Night Vision is a lightweight server-side data pack that grants all players a permanent Night Vision effect. Explore caves, mineshafts, and any dark area without needing Night Vision potions or placing torches everywhere. The effect is seamless and automatically applied on join.</p>
    <p>Compatible with all server setups — no client mod required. Supports Fabric, Forge, NeoForge, and vanilla Minecraft servers.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Permanent Night Vision for all players on the server</li>
      <li>Effect applies automatically on join and respawn</li>
      <li>No Night Vision potions or equipment needed</li>
      <li>Zero performance overhead — extremely lightweight</li>
      <li>Server-side only — no client mod required</li>
      <li>Works with Fabric, Forge, NeoForge, and Vanilla</li>
      <li>Supports Minecraft 1.14 through 1.21+</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge, Vanilla</td></tr>
      <tr><th>Minecraft</th><td>1.14 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── cave-vision-bedrock.html ──────────────────────────────────────────
Write-Page -File "cave-vision-bedrock.html" `
  -PageTitle "Cave Vision Bedrock – Permanent Night Vision Addon for Bedrock Edition" `
  -Desc "Cave Vision Bedrock is a lightweight Minecraft Bedrock Edition addon that gives all players infinite Night Vision, making cave exploration and dark areas completely visible without any equipment." `
  -Keywords "cave vision bedrock, night vision bedrock addon, mcpe night vision, infinite night vision bedrock, quillphen, bedrock edition" `
  -Icon "remove_red_eye" -IcColor "teal" `
  -Name "Cave Vision Bedrock" -Tagline "Infinite Night Vision for Bedrock Edition — see in any darkness" `
  -EdChip $bChip -TypChip $adChip `
  -MrUrl "https://modrinth.com/user/quillphen" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Cave Vision Bedrock is a lightweight Bedrock Edition behavior pack that grants all players a permanent infinite Night Vision effect. No potions, no torches, no config — just install and see in the dark. Ideal for cave exploration, underground building, and nighttime survival.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Permanent Night Vision for all players</li>
      <li>Effect applied automatically on world join and respawn</li>
      <li>No Night Vision potions or special equipment needed</li>
      <li>Works in caves, at night, and in The Nether and End</li>
      <li>Extremely lightweight — no performance impact</li>
      <li>Compatible with other Bedrock behavior packs</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Behavior Pack (Addon)</td></tr>
      <tr><th>Edition</th><td>Bedrock Edition (MCPE / Console / Windows)</td></tr>
      <tr><th>Minecraft</th><td>1.16+</td></tr>
    </table>
  </div>
'@

# ── enchantment-descriptions.html ────────────────────────────────────
Write-Page -File "enchantment-descriptions.html" `
  -PageTitle "Enchantment Descriptions – Detailed Enchantment Tooltips for Minecraft" `
  -Desc "Enchantment Descriptions is a Minecraft Java resource pack that adds detailed descriptions for every vanilla enchantment directly in the tooltip. Know exactly what each enchantment does before you apply it." `
  -Keywords "enchantment descriptions minecraft, minecraft enchantment tooltips, enchantment info resource pack, quillphen, java edition enchanting guide" `
  -Icon "auto_stories" -IcColor "pink" `
  -Name "Enchantment Descriptions" -Tagline "Detailed in-game tooltips for every Minecraft enchantment" `
  -EdChip $jChip -TypChip $rpChip `
  -MrUrl "https://modrinth.com/datapack/enchantment-descriptions-java" `
  -CfUrl "https://www.curseforge.com/minecraft/texture-packs/enchantment-descriptions-java" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Enchantment Descriptions enhances Minecraft's enchantment system by adding clear, detailed descriptions to every enchantment's tooltip. Hover over any enchanted item or book and instantly see what that enchantment does, its maximum level, and important compatibility notes.</p>
    <p>No more opening wikis mid-game. Perfect for new players learning enchantments and experienced players who need a quick reference.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Detailed descriptions for all vanilla enchantments</li>
      <li>Shows effect, behavior, and maximum levels</li>
      <li>Enchantment incompatibility notes included</li>
      <li>Covers weapon, tool, armor, bow, and special enchantments</li>
      <li>Works with enchanted books and enchanted items</li>
      <li>Compatible with Java Edition — no mod required</li>
      <li>Also available for Bedrock Edition on CurseForge</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">list</span>Enchantments Covered</h2>
    <ul class="feat-list">
      <li>Weapons: Sharpness, Knockback, Fire Aspect, Looting, Sweeping Edge, Smite, Bane of Arthropods</li>
      <li>Tools: Efficiency, Fortune, Silk Touch, Unbreaking, Mending</li>
      <li>Armor: Protection, Fire Protection, Blast Protection, Projectile Protection, Thorns, Feather Falling, Aqua Affinity, Respiration</li>
      <li>Bows: Power, Punch, Flame, Infinity</li>
      <li>Crossbows: Multishot, Piercing, Quick Charge</li>
      <li>Tridents: Loyalty, Riptide, Channeling, Impaling</li>
      <li>Special: Curse of Binding, Curse of Vanishing, Soul Speed, Swift Sneak, Frost Walker, Depth Strider</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Resource Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition (Bedrock on CurseForge)</td></tr>
      <tr><th>Minecraft</th><td>1.14 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── explosive-arrow.html (TNT Arrow) ─────────────────────────────────
Write-Page -File "explosive-arrow.html" `
  -PageTitle "TNT Arrow – Explosive Arrow Minecraft Data Pack" `
  -Desc "TNT Arrow is a Minecraft Java data pack that adds explosive TNT arrows that detonate on impact. Craft TNT arrows and use them for combat, mining, or just for fun. Server-side." `
  -Keywords "tnt arrow minecraft, explosive arrow datapack, minecraft bomb arrow, quillphen, fabric forge tnt arrow" `
  -Icon "rocket_launch" -IcColor "pink" `
  -Name "TNT Arrow" -Tagline "Explosive TNT arrows that detonate on impact — craft and unleash" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/tnt-arrow" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>TNT Arrow is a lightweight data pack that adds craftable explosive arrows to Minecraft. When shot, these arrows detonate on impact just like a TNT block — creating an explosion that damages entities and destroys terrain. Perfect for combat, sieges, and creative destruction.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Craftable TNT arrows with a custom recipe</li>
      <li>Arrows explode on impact with blocks or entities</li>
      <li>Explosion damages nearby mobs and destroys blocks</li>
      <li>Compatible with bows and crossbows</li>
      <li>Works in singleplayer and multiplayer</li>
      <li>Server-side — no client mod required</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.16 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── glowing-ore.html ─────────────────────────────────────────────────
Write-Page -File "glowing-ore.html" `
  -PageTitle "Glowing Ores – Animated Glowing Ore Resource Pack for Minecraft Java" `
  -Desc "Glowing Ores transforms all 18 Minecraft ore blocks into brilliant glowing treasures with a 5-tier intensity system, realistic color temperatures, and dynamic pulsing animations." `
  -Keywords "glowing ores minecraft, ore glow resource pack, animated ores java edition, quillphen, emissive ores minecraft, vanilla like ores" `
  -Icon "flare" -IcColor "amber" `
  -Name "Glowing Ores" -Tagline "All 18 ore types transformed into brilliant glowing blocks with pulsing animations" `
  -EdChip $jChip -TypChip $rpChip `
  -MrUrl "https://modrinth.com/resourcepack/glowing-ores-java" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Glowing Ores is a visually stunning resource pack that transforms all 18 Minecraft ore blocks into brilliant glowing treasures. Each ore type has a unique glow color and intensity level, making ores dramatically easier to spot while maintaining a beautiful, coherent aesthetic.</p>
    <p>Features a 5-tier intensity system ranging from subtle shimmer to brilliant glow, with realistic color temperatures and smooth dynamic pulsing animations that make ores feel alive.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>All 18 vanilla ore types with unique glow textures</li>
      <li>5-tier intensity system — from subtle to brilliant</li>
      <li>Realistic color temperatures matching each ore's material</li>
      <li>Dynamic pulsing animations on all ores</li>
      <li>High-resolution textures (512x or higher)</li>
      <li>Vanilla-like aesthetic — beautiful without being garish</li>
      <li>Compatible with Optifine and Iris for full emissive support</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">palette</span>Covered Ores</h2>
    <ul class="feat-list">
      <li>Diamond, Emerald, Gold, Iron, Coal, Copper, Lapis Lazuli, Redstone</li>
      <li>Nether Quartz, Nether Gold, Ancient Debris</li>
      <li>All stone and deepslate variants</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Resource Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Resolution</th><td>512x or higher</td></tr>
      <tr><th>Minecraft</th><td>1.17 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── insight-hud.html ─────────────────────────────────────────────────
Write-Page -File "insight-hud.html" `
  -PageTitle "Insight HUD – Entity Info and Equipment HUD Overlays for Minecraft" `
  -Desc "Insight HUD adds two essential HUD overlays for Minecraft Java Edition: detailed entity information and equipment condition tracking. Lightweight, configurable, and vanilla-aesthetic." `
  -Keywords "insight hud minecraft, entity info hud mod, equipment durability hud, quillphen, fabric forge client mod, minecraft hud overlay" `
  -Icon "dashboard" -IcColor "teal" `
  -Name "Insight HUD" -Tagline "Essential entity and equipment HUD overlays — clean and vanilla-friendly" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/insight-hud" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Insight HUD provides two essential HUD overlays that enhance your Minecraft experience while maintaining the vanilla aesthetic. The entity overlay shows detailed information about the mob or player you are looking at, including health, type, and status effects. The equipment overlay displays your held item stats and armor condition at a glance.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Entity info overlay: health, name, type, status effects</li>
      <li>Equipment overlay: held item and armor durability</li>
      <li>Clean, minimal design matching vanilla aesthetic</li>
      <li>Fully configurable position and display options</li>
      <li>Works on singleplayer and multiplayer servers</li>
      <li>Compatible with Fabric, Forge, and NeoForge</li>
      <li>Client-side — no server installation required</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge, NeoForge</td></tr>
      <tr><th>Minecraft</th><td>1.19 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── mob-vision.html ───────────────────────────────────────────────────
Write-Page -File "mob-vision.html" `
  -PageTitle "Mob Vision – See Glowing Mobs Through Walls in Minecraft" `
  -Desc "Mob Vision is a Minecraft Java data pack that applies a glowing effect to all mobs within a configurable radius, letting you spot enemies through walls and terrain. Server-side, no client mod." `
  -Keywords "mob vision minecraft, glowing mobs datapack, see mobs through walls, quillphen, mob detection datapack, fabric forge" `
  -Icon "person_search" -IcColor "amber" `
  -Name "Mob Vision" -Tagline "Detect all nearby mobs with a glowing effect visible through walls" `
  -EdChip $jChip -TypChip $dpChip `
  -MrUrl "https://modrinth.com/datapack/mobvision" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Mob Vision applies a persistent glowing effect to all mobs within a configurable radius around each player. The glow makes mobs visible through solid blocks and terrain, helping you navigate safely in caves and spot threats before they reach you. Useful for both PvE and PvP scenarios.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Glowing effect applied to all nearby mobs automatically</li>
      <li>Mobs visible through walls and solid blocks</li>
      <li>Configurable detection radius</li>
      <li>Works with hostile, passive, and neutral mobs</li>
      <li>Server-side — no client mod required</li>
      <li>Compatible with Fabric, Forge, NeoForge, and Vanilla</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Data Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.16 – 1.21+</td></tr>
      <tr><th>Side</th><td>Server-side</td></tr>
    </table>
  </div>
'@

# ── outlined-ores.html ────────────────────────────────────────────────
Write-Page -File "outlined-ores.html" `
  -PageTitle "Outlined Ores – Diamond Ore Outlines Resource Pack for Minecraft" `
  -Desc "Outlined Ores is a Minecraft Java resource pack that highlights diamond ore (and other ores) with magical glowing outlines for better visibility during mining. No X-ray needed." `
  -Keywords "outlined ores minecraft, diamond ore outline resource pack, ore visibility minecraft, quillphen, java edition resource pack" `
  -Icon "border_outer" -IcColor "teal" `
  -Name "Outlined Ores" -Tagline "Ore blocks highlighted with glowing outlines for instantly better visibility" `
  -EdChip $jChip -TypChip $rpChip `
  -MrUrl "https://modrinth.com/resourcepack/outlined-ores-java" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Outlined Ores is a resource pack that adds distinct glowing outlines to ore blocks in Minecraft Java Edition. Diamond ore, emerald ore, and other valuable ores stand out in the environment with a clear outline that makes them easy to spot without resorting to X-ray texture packs.</p>
    <p>Maintains vanilla textures while adding the visual clarity needed for efficient mining.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Glowing outlines on diamond, emerald, and other ores</li>
      <li>Distinct per-ore color coding for quick identification</li>
      <li>Maintains vanilla ore textures underneath the outline</li>
      <li>Works in stone, deepslate, and netherrack variants</li>
      <li>No X-ray or cheating — purely visual outline enhancement</li>
      <li>Client-side resource pack — works on any server</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Resource Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.17 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── potions-description.html ──────────────────────────────────────────
Write-Page -File "potions-description.html" `
  -PageTitle "Potions Description – Detailed Potion Tooltips for Minecraft" `
  -Desc "Potions Description is a Minecraft resource pack that adds detailed descriptions for every potion in the game directly in the tooltip. Know duration, strength, and effects before you brew." `
  -Keywords "potions description minecraft, potion tooltip resource pack, minecraft brewing guide, quillphen, java edition potions, potion info" `
  -Icon "science" -IcColor "purple" `
  -Name "Potions Description" -Tagline "Detailed tooltip descriptions for every Minecraft potion" `
  -EdChip $jChip -TypChip $rpChip `
  -MrUrl "https://modrinth.com/datapack/potions-description" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Potions Description adds clear, detailed tooltips to every potion in Minecraft. Hover over a potion and instantly see its effect, duration, strength level, and what it does to you or your enemies. No more consulting the wiki mid-brew — all the information you need is right in the tooltip.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Detailed descriptions for all vanilla potions</li>
      <li>Shows effect name, duration, and strength</li>
      <li>Covers all potion types: base, splash, and lingering</li>
      <li>Works with regular, extended, and enhanced versions</li>
      <li>Includes negative/debuff potion descriptions</li>
      <li>Client-side resource pack — works on any server</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Resource Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.14 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── smart-arrows.html ─────────────────────────────────────────────────
Write-Page -File "smart-arrows.html" `
  -PageTitle "Smart Arrows – Ricochet and Teleportation Arrow Mechanics in Minecraft" `
  -Desc "Smart Arrows adds advanced arrow mechanics to Minecraft including ricochet physics (arrows bounce off surfaces) and teleportation (arrows teleport the shooter on impact). Fabric mod." `
  -Keywords "smart arrows minecraft, ricochet arrow mod, teleport arrow minecraft, quillphen, fabric mod arrows, arrow mechanics" `
  -Icon "arrow_forward" -IcColor "teal" `
  -Name "Smart Arrows" -Tagline "Arrows that ricochet off walls and teleport the shooter on impact" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/smart-arrows" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Smart Arrows overhauls Minecraft arrow mechanics with two unique abilities. Ricochet arrows bounce off solid surfaces, letting you shoot around corners and hit targets from unexpected angles. Teleport arrows teleport the shooter to the arrow's impact point, enabling swift and deadly repositioning in combat.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Ricochet: arrows bounce off walls and surfaces</li>
      <li>Teleportation: arrows teleport the shooter to the impact point</li>
      <li>Multiple arrow types with different behaviors</li>
      <li>Craftable or obtainable through gameplay</li>
      <li>Works with bows and crossbows</li>
      <li>Compatible with Fabric loader</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric</td></tr>
      <tr><th>Minecraft</th><td>1.19 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client &amp; Server</td></tr>
    </table>
  </div>
'@

# ── smithing-templates-descriptions.html ────────────────────────────
Write-Page -File "smithing-templates-descriptions.html" `
  -PageTitle "Smithing Templates Descriptions – Detailed Tooltips for Smithing Templates" `
  -Desc "Smithing Templates Descriptions is a Minecraft Fabric mod that replaces smithing template item names with detailed multi-line descriptions including their usage, duplication recipe, and lore." `
  -Keywords "smithing templates descriptions minecraft, smithing template tooltips, minecraft armor trim descriptions, quillphen, fabric mod smithing" `
  -Icon "description" -IcColor "blue" `
  -Name "Smithing Templates Descriptions" -Tagline "Smithing templates with detailed in-game usage, duplication, and lore descriptions" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/smithing-templates-descriptions" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Smithing Templates Descriptions replaces the generic smithing template item names with detailed, multi-line tooltip descriptions. Each template shows exactly what upgrade or armor trim it applies, its duplication recipe, and associated lore — offering clarity that goes beyond what a resource pack can achieve.</p>
    <p>This is a Fabric mod (not a resource pack), so the descriptions are injected directly into the item data for accurate and complete display.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Detailed multi-line descriptions for all smithing templates</li>
      <li>Shows the upgrade or armor trim applied by each template</li>
      <li>Includes the duplication recipe ingredients</li>
      <li>Lore text providing context and flavor</li>
      <li>Works for all vanilla armor trim and netherite upgrade templates</li>
      <li>Client-side — works on any server</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric</td></tr>
      <tr><th>Minecraft</th><td>1.20 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── x-ray-java.html ───────────────────────────────────────────────────
Write-Page -File "x-ray-java.html" `
  -PageTitle "X-RAY Java Edition – Ore Visibility Resource Pack for Minecraft" `
  -Desc "X-RAY Java Edition is a Minecraft resource pack that makes stone and most blocks semi-transparent while highlighting all ore types, making resource location fast and easy." `
  -Keywords "x-ray minecraft java, x-ray resource pack, ore finder minecraft, transparent stone resource pack, quillphen, ore visibility pack" `
  -Icon "visibility" -IcColor "pink" `
  -Name "X-RAY Java Edition" -Tagline "See through stone to locate every ore type — resource pack for Java Edition" `
  -EdChip $jChip -TypChip $rpChip `
  -MrUrl "https://modrinth.com/user/quillphen" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>X-RAY Java Edition is a resource pack that replaces stone, dirt, and other filler blocks with transparent or semi-transparent textures, exposing all ore deposits within view range. Perfect for quickly locating diamonds, ancient debris, and other valuable resources.</p>
    <p>Install as a standard resource pack — no mods required. Works in singleplayer and can be toggled on or off.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Stone, dirt, gravel, and other filler blocks become transparent</li>
      <li>All ore types clearly visible against transparent background</li>
      <li>Works in the Overworld, Nether, and End</li>
      <li>No mod required — pure resource pack</li>
      <li>Toggle on or off via the resource pack menu</li>
      <li>Compatible with Java Edition 1.17+</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Resource Pack</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Minecraft</th><td>1.17 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client-side</td></tr>
    </table>
  </div>
'@

# ── ai-crafter.html (Minecraft AI Assistant) ─────────────────────────
Write-Page -File "ai-crafter.html" `
  -PageTitle "Minecraft AI Assistant – Google Gemini AI Integrated into Minecraft" `
  -Desc "Minecraft AI Assistant brings Google Gemini AI directly into your Minecraft world. Ask questions, get instant help, and execute commands through natural language — powered by Gemini AI." `
  -Keywords "minecraft ai assistant, minecraft gemini ai, ai in minecraft, natural language commands minecraft, quillphen, fabric forge ai mod" `
  -Icon "smart_toy" -IcColor "purple" `
  -Name "Minecraft AI Assistant" -Tagline "Google Gemini AI directly inside Minecraft — ask anything, command anything" `
  -EdChip $jChip -TypChip $modChip `
  -MrUrl "https://modrinth.com/mod/minecraft-ai-assistant" `
  -Body @'
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Description</h2>
    <p>Minecraft AI Assistant integrates Google Gemini AI directly into your Minecraft experience. Type natural language questions or commands in the game chat and receive instant, intelligent responses from Gemini AI. Get crafting recipes, building suggestions, mob tips, command help, or just have a conversation — all without leaving the game.</p>
    <p>Requires a Google Gemini API key (free tier available). The mod securely sends your queries to Gemini and displays the response in chat.</p>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">check_circle</span>Features</h2>
    <ul class="feat-list">
      <li>Google Gemini AI integrated directly into Minecraft chat</li>
      <li>Ask any question in natural language</li>
      <li>Execute Minecraft commands by describing them</li>
      <li>Crafting recipe lookups, building tips, and mob info</li>
      <li>Real-time AI responses without leaving the game</li>
      <li>Configurable system prompt for custom AI behavior</li>
      <li>Compatible with Fabric and Forge</li>
    </ul>
  </div>
  <div class="card-section">
    <h2><span class="msrnd" aria-hidden="true">info</span>Specifications</h2>
    <table class="specs-table">
      <tr><th>Type</th><td>Mod</td></tr>
      <tr><th>Edition</th><td>Java Edition</td></tr>
      <tr><th>Loaders</th><td>Fabric, Forge</td></tr>
      <tr><th>Minecraft</th><td>1.20 – 1.21+</td></tr>
      <tr><th>Side</th><td>Client &amp; Server</td></tr>
      <tr><th>Requires</th><td>Google Gemini API Key (free)</td></tr>
    </table>
  </div>
'@

Write-Host "`nAll pages generated successfully!"
Get-ChildItem $dir -Filter "*.html" | Measure-Object | Select-Object Count
