"""
QuillPhen site fixer:
 1. Cleans index.html (removes ad scripts/divs, keeps analytics)
 2. Rewrites all old project pages to MD3 design
 3. Creates all missing project pages
 4. Updates sitemap.xml
"""
import re, os

BASE = r"d:\mc packs\sites\revmap\quillphen"

# ─── SHARED COMPONENTS ────────────────────────────────────────────────────────

GA = """  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3W2T4M8K8"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-K3W2T4M8K8');</script>"""

TOPBAR = """<header class="top-bar" id="top-bar">
  <div class="bar-inner">
    <a href="index.html" class="bar-brand">
      <div class="bar-avatar">
        <img src="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp" alt="QuillPhen" width="36" height="36" loading="eager">
      </div>
      <span class="bar-name">QuillPhen</span>
    </a>
    <nav class="bar-nav">
      <a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener" class="btn-nav">
        <svg viewBox="0 0 512 514" aria-hidden="true" style="fill:currentColor;width:16px;height:16px;flex-shrink:0"><path d="M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"/></svg>
        <span>Modrinth</span>
      </a>
      <a href="https://www.curseforge.com/members/quillphen/projects" target="_blank" rel="noopener" class="btn-nav">CurseForge</a>
    </nav>
  </div>
</header>"""

FOOTER = """<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <a href="index.html" class="bar-brand">
        <div class="bar-avatar"><img src="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp" alt="QuillPhen" width="36" height="36" loading="lazy"></div>
        <span class="bar-name">QuillPhen</span>
      </a>
      <p>Quality-of-life Minecraft mods, data packs, resource packs and shaders for Java &amp; Bedrock Edition.</p>
    </div>
    <div>
      <p class="footer-col-title">Links</p>
      <ul class="footer-links">
        <li><a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener">Modrinth Profile</a></li>
        <li><a href="https://www.curseforge.com/members/quillphen/projects" target="_blank" rel="noopener">CurseForge Profile</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
        <li><a href="rss.xml">RSS Feed</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">Categories</p>
      <ul class="footer-links">
        <li><a href="index.html#projects">Data Packs</a></li>
        <li><a href="index.html#projects">Mods</a></li>
        <li><a href="index.html#projects">Resource Packs</a></li>
        <li><a href="index.html#projects">Shaders</a></li>
        <li><a href="index.html#projects">Bedrock Addons</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 QuillPhen. Not affiliated with Mojang or Microsoft.</p>
    <div class="footer-bottom-links">
      <a href="robots.txt">Robots</a>
      <a href="sitemap.xml">Sitemap</a>
    </div>
  </div>
</footer>"""

PAGE_JS = """<script>
const topBar=document.getElementById('top-bar');
window.addEventListener('scroll',()=>{topBar.classList.toggle('scrolled',window.scrollY>8);},{passive:true});
</script>"""

TYPE_LABELS = {
    'datapack': 'Data Pack', 'mod': 'Mod', 'resourcepack': 'Resource Pack',
    'shader': 'Shader', 'addon': 'Bedrock Addon'
}
EDITION_LABELS = {'java': 'Java Edition', 'bedrock': 'Bedrock Edition'}

MDR_SVG = '<svg viewBox="0 0 512 514" aria-hidden="true" style="fill:currentColor;width:15px;height:15px;flex-shrink:0"><path d="M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"/></svg>'

# ─── PROJECT DATA ─────────────────────────────────────────────────────────────

PROJECTS = [
{
    'id': 'tree-vein-miner', 'title': 'Tree Vein Miner', 'type': 'datapack', 'edition': 'java',
    'icon': 'forest', 'ic': '', 'mr': 'https://modrinth.com/datapack/tree-vein-miner', 'pg': 'tree-vein-miner.html',
    'desc': 'Removes entire trees — logs and leaves — when you crouch and break a log. Smart and efficient.',
    'tagline': 'Fell entire trees with a single crouched break',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Breaks all connected logs of the same type instantly',
        'Removes leaves automatically — no orphaned floaters',
        'Activate by crouching while mining a log',
        'Respects Fortune and Silk Touch enchantments',
        'Works on all vanilla and modded wood types',
        'Zero performance impact — pure command-based logic',
    ],
    'extra': '<p>Simply sneak and break any log to instantly clear the entire tree, leaves included. Ideal for survival players, SMP servers, and anyone tired of floating leaf islands.</p>',
},
{
    'id': 'ore-vein-miner', 'title': 'Ore Vein Miner', 'type': 'datapack', 'edition': 'java',
    'icon': 'diamond', 'ic': 'teal', 'mr': 'https://modrinth.com/datapack/ore-vein-miner', 'pg': 'ore-vein-miner.html',
    'desc': 'Automatically mines all connected ore blocks of the same type when you break one.',
    'tagline': 'Mine entire ore veins in a single swing',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Mines entire connected veins of the same ore type',
        'Proper Fortune and Silk Touch support',
        'Triggered by crouching while mining',
        'Handles all vanilla ores including deepslate variants',
        'No mod loader required — pure data pack',
        'SMP compatible — works for all players',
    ],
    'extra': '<p>Never miss a vein again. One crouch-break clears the entire connected ore cluster, giving you all drops with the correct enchantment bonuses applied.</p>',
},
{
    'id': 'vein-miner', 'title': 'VeinMiner', 'type': 'datapack', 'edition': 'java',
    'icon': 'hardware', 'ic': '', 'mr': 'https://modrinth.com/datapack/vein_miner', 'pg': 'vein-miner.html',
    'desc': 'Mine entire ore veins and fell whole trees efficiently. A lightweight chain-mining data pack.',
    'tagline': 'Combined ore and tree chain-mining in one pack',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Chain-mines entire ore veins from one break',
        'Fells complete trees — logs and leaves',
        'Respects tool enchantments (Fortune, Silk Touch)',
        'Crouch-to-activate for full player control',
        'Compatible with all vanilla wood and ore types',
        'Minimal overhead, pure data pack implementation',
    ],
    'extra': '<p>The all-in-one vein mining solution. Combines tree felling and ore vein mining into a single lightweight data pack without any mod dependencies.</p>',
},
{
    'id': 'cave-vision', 'title': 'Night Vision', 'type': 'datapack', 'edition': 'java',
    'icon': 'remove_red_eye', 'ic': '', 'mr': 'https://modrinth.com/datapack/cave-vision', 'pg': 'cave-vision.html',
    'desc': 'Grants all players permanent Night Vision — caves and dark areas are effortlessly bright.',
    'tagline': 'Permanent Night Vision for every player',
    'versions': '1.14 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Grants perpetual Night Vision to all online players',
        'No potions, no brewing stands required',
        'Works in caves, the Nether, and the End',
        'Automatically re-applies if the effect expires',
        'Zero performance cost — lightweight tick loop',
        'Compatible with every SMP and singleplayer world',
    ],
    'extra': '<p>Stop carrying stacks of Night Vision potions. This data pack runs quietly in the background and keeps every player permanently lit — ideal for mining worlds and adventure servers.</p>',
},
{
    'id': 'enchantment-descriptions', 'title': 'Enchantment Descriptions', 'type': 'resourcepack', 'edition': 'java',
    'icon': 'auto_stories', 'ic': 'pink', 'mr': 'https://modrinth.com/datapack/enchantment-descriptions-java', 'pg': 'enchantment-descriptions.html',
    'desc': 'Adds detailed descriptions for every vanilla enchantment directly in the tooltip.',
    'tagline': 'Know exactly what every enchantment does',
    'versions': '1.20 – 1.21+', 'loader': 'Resource Pack (no mods needed)',
    'features': [
        'Tooltip descriptions for all 40+ vanilla enchantments',
        'Clear, concise language — no wiki required',
        'Shows compatibility, max level, and effect details',
        'Works with any mod loader or vanilla',
        'Drag-and-drop installation — no setup needed',
        'Updated for the latest Minecraft versions',
    ],
    'extra': '<p>Every enchantment in the game gets a plain-English tooltip explaining exactly what it does, how strong each level is, and what it is incompatible with.</p>',
},
{
    'id': 'vein-miner-preview', 'title': 'Vein Miner & Preview', 'type': 'datapack', 'edition': 'java',
    'icon': 'preview', 'ic': 'teal', 'mr': 'https://modrinth.com/datapack/the-vein-miner', 'pg': 'vein-miner-preview.html',
    'desc': 'Universal vein miner supporting Silk Touch, durability handling, and visual previews on 1.14–1.21+.',
    'tagline': 'Vein mining with real-time visual preview',
    'versions': '1.14 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Mines full ore veins in a single break',
        'Visual preview shows which blocks will be mined',
        'Fortune and Silk Touch enchantment support',
        'Tool durability is correctly consumed per block',
        'Crouch to activate, works per-player',
        'Broad version support from 1.14 through 1.21+',
    ],
    'extra': '<p>The most advanced vein mining data pack with a live visual preview overlay showing exactly which blocks will be collected before you commit to the break.</p>',
},
{
    'id': 'glowing-ore', 'title': 'Glowing Ores', 'type': 'resourcepack', 'edition': 'java',
    'icon': 'flare', 'ic': 'amber', 'mr': 'https://modrinth.com/resourcepack/glowing-ores-java', 'pg': 'glowing-ore.html',
    'desc': 'Transforms all 18 ore blocks into brilliant glowing treasures with a 5-tier intensity system.',
    'tagline': 'Every ore block glows with pulsing emissive light',
    'versions': '1.17 – 1.21+', 'loader': 'Resource Pack (OptiFine / Iris recommended)',
    'features': [
        'Emissive glow textures for all 18 ore variants',
        'Normal and deepslate ore variants covered',
        'Five hand-tuned intensity tiers by ore rarity',
        'Pulsing animation on diamond and netherite ores',
        'Compatible with OptiFine and Iris shaders',
        'Clean, readable design — not oversaturated',
    ],
    'extra': '<p>Coal glows dimly, iron shines steadily, diamonds pulse with an electric brilliance. All 18 ore types — including their deepslate forms — receive individually tuned emissive textures.</p>',
},
{
    'id': 'dynamic-lighting', 'title': 'Dynamic Lighting', 'type': 'datapack', 'edition': 'java',
    'icon': 'flashlight_on', 'ic': 'amber', 'mr': 'https://modrinth.com/datapack/dynamic-lighting', 'pg': 'dynamic-lighting.html',
    'desc': 'Emits real-time light from held light-emitting items and glowing entities — no mods required.',
    'tagline': 'Held torches and lanterns actually light your way',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Light sources held in hand illuminate nearby blocks',
        'Supports torches, lanterns, glowstone, sea lanterns, and more',
        'Glowing entities (spectral arrows, magma cubes) emit light',
        'No OptiFine or Sodium/Iris required',
        'Smooth interpolation as you move',
        'Compatible with all game modes and dimensions',
    ],
    'extra': '<p>Experience true dynamic lighting with a pure data pack — no mods, no shaders. Walk through the Nether holding a torch and watch the light move with you.</p>',
},
{
    'id': 'tree-veinminer-enchant', 'title': 'Tree Veinminer Enchantment', 'type': 'datapack', 'edition': 'java',
    'icon': 'auto_fix_high', 'ic': 'amber', 'mr': 'https://modrinth.com/datapack/tree-veinminer-enchant', 'pg': 'tree-veinminer-enchant.html',
    'desc': 'Adds a Tree Veinminer enchantment for axes — instantly fell entire trees with a single chop.',
    'tagline': 'Enchant your axe to fell whole trees at once',
    'versions': '1.20 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'New Tree Veinminer enchantment available for axes',
        'Fells the entire connected tree instantly on break',
        'Obtainable via enchanting table and loot tables',
        'Balances power with durability cost per log',
        'Leaves clean up automatically after the trunk falls',
        'Works with all vanilla and supported modded wood types',
    ],
    'extra': '<p>Instead of crouching, this pack adds a real enchantment to the game. Find it on enchanting tables, use it on any axe, and every tree becomes a single-hit harvest.</p>',
},
{
    'id': 'explosive-arrow', 'title': 'TNT Arrow', 'type': 'datapack', 'edition': 'java',
    'icon': 'rocket_launch', 'ic': 'pink', 'mr': 'https://modrinth.com/datapack/tnt-arrow', 'pg': 'explosive-arrow.html',
    'desc': 'Adds explosive TNT arrows that detonate on impact. Great for combat and rapid terrain clearing.',
    'tagline': 'Explosive arrows that detonate on impact',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'TNT arrows explode on impact with any surface or entity',
        'Configurable explosion radius and power',
        'Craft TNT arrows with a simple recipe',
        'Deals AoE damage — effective in mob farms and PvP',
        'Explosion particles and sound effects included',
        'Toggle mob griefing to control terrain damage',
    ],
    'extra': '<p>Combine the Bow with explosive payloads. TNT Arrows add a new arrow type that detonates on contact — great for combat, demolition, and chaotic creative sessions.</p>',
},
{
    'id': 'potions-description', 'title': 'Potions Description', 'type': 'resourcepack', 'edition': 'java',
    'icon': 'science', 'ic': 'purple', 'mr': 'https://modrinth.com/datapack/potions-description', 'pg': 'potions-description.html',
    'desc': 'Provides clear, detailed tooltip descriptions for every potion in the game.',
    'tagline': 'Every potion explained in plain language',
    'versions': '1.20 – 1.21+', 'loader': 'Resource Pack (no mods needed)',
    'features': [
        'Tooltip text for every brewed and splash potion',
        'Shows duration, potency, and effect description',
        'Covers all vanilla potion types including extended/enhanced',
        'Lingering and splash variants included',
        'Works without any mod loader',
        'Drag-and-drop installation — no config required',
    ],
    'extra': '<p>Stop hovering over potions trying to remember what they do. Every potion bottle gets a clear tooltip showing its effect, duration, and strength at a glance.</p>',
},
{
    'id': 'dynamic-light-shader', 'title': 'Dynamic Light Shader', 'type': 'shader', 'edition': 'java',
    'icon': 'auto_awesome', 'ic': 'amber', 'mr': 'https://modrinth.com/shader/dynamic-light-shader', 'pg': 'dynamic-light-shader.html',
    'desc': 'Lightweight Iris/OptiFine shader that makes held items emit visible light with a glow bloom.',
    'tagline': 'Shader-quality glow bloom for held light sources',
    'versions': '1.17 – 1.21+', 'loader': 'OptiFine / Iris (Sodium)',
    'features': [
        'Realistic bloom glow from held torches and lanterns',
        'Minimal performance cost — highly optimised GLSL',
        'Compatible with Iris (Sodium) and OptiFine',
        'Configurable bloom radius and intensity',
        'Stacks nicely with other shader packs',
        'Works in all dimensions',
    ],
    'extra': '<p>A purpose-built shader layer that adds only the dynamic lighting bloom effect, letting you combine it with your favourite performance shader without sacrificing FPS.</p>',
},
{
    'id': 'auto-builder', 'title': 'Auto Builder', 'type': 'datapack', 'edition': 'java',
    'icon': 'construction', 'ic': 'teal', 'mr': 'https://modrinth.com/datapack/auto-bridge', 'pg': 'auto-builder.html',
    'desc': 'Automatically places blocks beneath you as you walk forward — perfect for bridges and paths.',
    'tagline': 'Auto-bridge and path builder as you walk',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Automatically places the held block under your feet',
        'Walk forward over any gap to instantly bridge',
        'Works with any solid buildable block',
        'Activate by crouching while walking',
        'No mod loader required',
        'Great for sky bridges, parkour maps, and SMP',
    ],
    'extra': '<p>Speed-bridge without the precision finger work. Hold a block, crouch-walk forward, and it places automatically under your feet — seamlessly spanning any gap.</p>',
},
{
    'id': 'outlined-ores', 'title': 'Outlined Ores', 'type': 'resourcepack', 'edition': 'java',
    'icon': 'border_outer', 'ic': 'teal', 'mr': 'https://modrinth.com/resourcepack/outlined-ores-java', 'pg': 'outlined-ores.html',
    'desc': 'Highlights ore blocks with glowing outlines for better visibility without X-ray cheating.',
    'tagline': 'Glowing outlines on all ore blocks for easy spotting',
    'versions': '1.17 – 1.21+', 'loader': 'Resource Pack (OptiFine / Iris recommended)',
    'features': [
        'High-contrast outlines on all 18 ore variants',
        'Visible against stone, deepslate, and netherrack',
        'Unique colour per ore type for fast recognition',
        'Works with emissive-compatible shaders for extra glow',
        'No X-ray — outlines only appear on exposed faces',
        'Compatible with most other texture packs',
    ],
    'extra': '<p>Outlined Ores adds bright, colour-coded borders to exposed ore faces. Spot diamonds at a glance without touching X-ray clients — perfectly legitimate to use on any server.</p>',
},
{
    'id': 'mob-capture-orb', 'title': 'Mob Capture ORB', 'type': 'mod', 'edition': 'java',
    'icon': 'cruelty_free', 'ic': 'amber', 'mr': 'https://modrinth.com/mod/mob-capture-orb', 'pg': 'mob-capture-orb.html',
    'desc': 'Capture any mob in a magical orb, carry it in your inventory, and release it wherever you want.',
    'tagline': 'Capture, carry, and release any mob with an orb',
    'versions': '1.20 – 1.21+', 'loader': 'Fabric / Forge / NeoForge',
    'features': [
        'Capture any mob — passive, neutral, and hostile',
        'Captured mobs are stored as inventory items',
        'Mob health, equipment, and NBT data are preserved',
        'Craftable orbs with simple recipe',
        'Release precisely by right-clicking any surface',
        'Compatible with all major Fabric / Forge loaders',
    ],
    'extra': '<p>The Mob Capture Orb lets you pick up any entity and carry it in your pocket. Relocate livestock, rescue rare mobs, or transport villagers — all without a minecart.</p>',
},
{
    'id': 'auto-replant-crops', 'title': 'Auto Replant Crops', 'type': 'datapack', 'edition': 'java',
    'icon': 'grass', 'ic': '', 'mr': 'https://modrinth.com/datapack/auto-replant-crops', 'pg': 'auto-replant-crops.html',
    'desc': 'Automatically replants fully grown crops after harvesting. Lightweight QoL for any survival or SMP server.',
    'tagline': 'Harvest without replanting — crops regrow automatically',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Harvesting a mature crop automatically replants it',
        'Works for wheat, carrots, potatoes, beetroot, and more',
        'Seeds consumed from inventory on replant',
        'If no seeds available, crop item drops normally',
        'Zero performance cost on large farms',
        'SMP-friendly — per-player seed inventory check',
    ],
    'extra': '<p>The most tedious part of crop farming is gone. Right-click a mature crop, it drops its items and immediately plants a new seed — as long as you have seeds in your inventory.</p>',
},
{
    'id': 'ore-veinminer-enchant', 'title': 'Ore Veinminer Enchantment', 'type': 'datapack', 'edition': 'java',
    'icon': 'auto_fix_high', 'ic': 'teal', 'mr': 'https://modrinth.com/datapack/ore-veinminer-enchant', 'pg': 'ore-veinminer-enchant.html',
    'desc': 'Adds an Ore Veinminer enchantment for pickaxes — instantly mine entire ore veins with one swing.',
    'tagline': 'Enchant your pickaxe to clear full ore veins',
    'versions': '1.20 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'New Ore Veinminer enchantment for pickaxes',
        'Mines the entire connected vein on a single break',
        'Obtainable at the enchanting table',
        'Fortune and Silk Touch work on the full vein',
        'Durability cost scales with blocks mined',
        'Works for all vanilla and deepslate ore variants',
    ],
    'extra': '<p>Upgrade your pickaxe with the Ore Veinminer enchantment and let every ore break cascade through the entire exposed vein — no crouching required.</p>',
},
{
    'id': 'coordinates-hud', 'title': 'Coordinates HUD', 'type': 'mod', 'edition': 'java',
    'icon': 'gps_fixed', 'ic': 'blue', 'mr': 'https://modrinth.com/mod/coordinateshud', 'pg': 'coordinates-hud.html',
    'desc': 'Advanced coordinate display mod with fully customizable HUD showing coordinates, biome, compass direction, and more.',
    'tagline': 'Clean, configurable coordinates and biome HUD',
    'versions': '1.20 – 1.21+', 'loader': 'Fabric / Forge / NeoForge',
    'features': [
        'Real-time X, Y, Z coordinate display',
        'Current biome name and dimension shown',
        'Compass direction and facing angle',
        'Fully configurable position, size, and colour',
        'Toggle HUD visibility with a keybind',
        'Minimal performance impact',
    ],
    'extra': '<p>Always know where you are. Coordinates HUD adds a sleek, unobtrusive overlay with your current position, biome, and facing direction — fully customisable to your preference.</p>',
},
{
    'id': 'ai-crafter', 'title': 'Minecraft AI Assistant', 'type': 'mod', 'edition': 'java',
    'icon': 'smart_toy', 'ic': 'purple', 'mr': 'https://modrinth.com/mod/minecraft-ai-assistant', 'pg': 'ai-crafter.html',
    'desc': 'Brings Google Gemini AI into Minecraft — ask questions, get help, and execute commands via natural language.',
    'tagline': 'Google Gemini AI as your Minecraft companion',
    'versions': '1.21.5+', 'loader': 'Fabric / Forge / NeoForge / Quilt',
    'features': [
        'Ask any Minecraft question in natural language via /ai',
        'Execute commands by describing them via /aic',
        'Powered by Google Gemini 2.5 Flash and Pro',
        'API key stored locally — no data collected',
        'Survival-mode protection blocks cheat commands',
        'Configure via in-game menu (K key)',
    ],
    'extra': '''<p>Minecraft AI Assistant embeds the Google Gemini AI directly into the game. Ask questions like "what level do diamonds spawn?" or tell it "give me 64 torches" and it will run the command for you.</p>
<div class="card-section" style="margin-top:1rem;background:color-mix(in srgb,var(--md-tertiary-container) 40%,var(--surface-lowest))">
  <h2><span class="msrnd">key</span>API Key Required</h2>
  <p>This mod requires a free Google Gemini API key from <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Google AI Studio</a>. Press <strong>K</strong> in-game to open the config and paste your key.</p>
</div>''',
},
{
    'id': 'mob-vision', 'title': 'Mob Vision', 'type': 'datapack', 'edition': 'java',
    'icon': 'person_search', 'ic': 'amber', 'mr': 'https://modrinth.com/datapack/mobvision', 'pg': 'mob-vision.html',
    'desc': 'Applies a glowing effect to mobs near you so you can spot enemies through walls within a configurable radius.',
    'tagline': 'See nearby mobs through walls with a glow effect',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Applies Glowing status to all mobs within range',
        'Configurable detection radius (default 20 blocks)',
        'Works on all hostile, neutral, and passive mobs',
        'Glowing effect is removed when mob moves out of range',
        'No mod loader required',
        'Useful for caving, raiding, and PvP servers',
    ],
    'extra': '<p>Mob Vision scans your surroundings every tick and tags nearby entities with the Glowing effect, letting you see their outline through blocks — an invaluable cave exploration tool.</p>',
},
{
    'id': 'waypoints', 'title': 'Waypoints & Teleport', 'type': 'datapack', 'edition': 'java',
    'icon': 'place', 'ic': 'pink', 'mr': 'https://modrinth.com/datapack/waypoints-teleport', 'pg': 'waypoints.html',
    'desc': 'Lightweight survival-friendly waypoint system with fast travel and teleports for singleplayer and SMP. Java 1.21.6+.',
    'tagline': 'Save locations and teleport between them in survival',
    'versions': '1.21.6+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Set named waypoints anywhere in the world',
        'Teleport to any saved waypoint instantly',
        'Per-player waypoint storage — private to each player',
        'Works in all dimensions — Overworld, Nether, End',
        'List and delete waypoints via simple commands',
        'No mods required — pure vanilla commands',
    ],
    'extra': '<p>Mark your base, your mine, and your farm, then zip between them in seconds. Waypoints & Teleport brings fast travel to vanilla survival without breaking immersion.</p>',
},
{
    'id': 'insight-hud', 'title': 'Insight HUD', 'type': 'mod', 'edition': 'java',
    'icon': 'dashboard', 'ic': 'teal', 'mr': 'https://modrinth.com/mod/insight-hud', 'pg': 'insight-hud.html',
    'desc': 'Two essential HUD overlays showing detailed entity information and equipment stats — clean and vanilla-friendly.',
    'tagline': 'Entity info and gear stats in a clean overlay',
    'versions': '1.20 – 1.21+', 'loader': 'Fabric / Forge / NeoForge',
    'features': [
        'Gear & Item Insight: live durability and stats for held/worn items',
        'Combat HUD: target health and loot table while in battle',
        'Minimalist design — no screen clutter',
        'Toggle each module independently (H key)',
        'Fully configurable position and appearance',
        'Lightweight — minimal performance cost',
    ],
    'extra': '<p>Insight HUD gives you two clean overlays in one mod: one for your gear and one for whatever entity you are fighting. Press H to open settings and toggle each panel on or off.</p>',
},
{
    'id': 'smithing-templates-descriptions', 'title': 'Smithing Templates Descriptions', 'type': 'mod', 'edition': 'java',
    'icon': 'description', 'ic': 'blue', 'mr': 'https://modrinth.com/mod/smithing-templates-descriptions', 'pg': 'smithing-templates-descriptions.html',
    'desc': 'Replaces smithing template names with detailed multi-line descriptions including usage, duplication, and lore.',
    'tagline': 'Full descriptions on every smithing template item',
    'versions': '1.20 – 1.21+', 'loader': 'Fabric / Forge / NeoForge',
    'features': [
        'Every smithing template gets a multi-line tooltip',
        'Shows the armor/weapon upgrade effect it applies',
        'Duplication recipe shown inline in the tooltip',
        'Where to find it — biome and structure hint',
        'Lore text for Netherite Upgrade and trims',
        'Works out of the box with no configuration',
    ],
    'extra': '<p>Smithing Templates are powerful but obscure. This mod adds rich tooltip text to every template — telling you what it does, how to duplicate it, and where to find more.</p>',
},
{
    'id': 'stackable-item', 'title': 'Stackable Item', 'type': 'datapack', 'edition': 'java',
    'icon': 'inventory_2', 'ic': 'blue', 'mr': 'https://modrinth.com/datapack/stackable-item', 'pg': 'stackable-item.html',
    'desc': 'Makes potions, boats, saddles, totems, and more stackable — keep your inventory clean and organised.',
    'tagline': 'Stack potions, saddles, totems, and more',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Potions stack up to 16 per slot',
        'Saddles, boats, minecarts, and name tags stack',
        'Totems of Undying and shields stack',
        'Ender pearls and snowballs stack to 64',
        'No mod loader required',
        'Reduces inventory clutter dramatically',
    ],
    'extra': '<p>Stop wasting inventory slots on single items. Stackable Item makes dozens of normally non-stackable items behave sensibly — potions, saddles, totems — all neatly stacked.</p>',
},
{
    'id': 'smart-arrows', 'title': 'Smart Arrows', 'type': 'mod', 'edition': 'java',
    'icon': 'arrow_forward', 'ic': 'teal', 'mr': 'https://modrinth.com/mod/smart-arrows', 'pg': 'smart-arrows.html',
    'desc': 'Arrow mechanics overhaul — arrows can ricochet off surfaces and teleport the shooter on contact.',
    'tagline': 'Ricocheting and teleporting arrow mechanics',
    'versions': '1.20 – 1.21+', 'loader': 'Fabric / Forge / NeoForge',
    'features': [
        'Arrows ricochet off hard surfaces at realistic angles',
        'Special arrow types: Teleport (blink to impact point)',
        'Configurable ricochet count and friction',
        'Compatible with existing enchantments (Flame, Power, etc.)',
        'New crafting recipes for special arrow variants',
        'Works on multiplayer servers',
    ],
    'extra': '<p>Smart Arrows reinvents ranged combat. Shoot around corners with ricochets, blink to the impact point with teleport arrows, and dominate with physics-driven shots.</p>',
},
{
    'id': 'automatic-smelt', 'title': 'Automatic Smelt', 'type': 'datapack', 'edition': 'java',
    'icon': 'local_fire_department', 'ic': 'amber', 'mr': 'https://modrinth.com/datapack/automatic-smelt', 'pg': 'automatic-smelt.html',
    'desc': 'Every block you mine that can be smelted automatically drops its smelted form — no furnace needed.',
    'tagline': 'Mine blocks and get their smelted drops instantly',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Auto-smelts ore blocks (raw iron, gold, copper) on break',
        'Sand drops glass, cobblestone drops stone, etc.',
        'Works with Fortune for bonus drops',
        'Activates when you have the correct tool in hand',
        'No furnaces needed for common smelting tasks',
        'Toggle via simple in-game command',
    ],
    'extra': '<p>Skip the furnace queue. Automatic Smelt processes smeltable blocks at the point of mining — raw ores become ingots, sand becomes glass, all without a single furnace slot used.</p>',
},
{
    'id': 'custom-vein-miner', 'title': 'Custom Vein Miner', 'type': 'datapack', 'edition': 'java',
    'icon': 'tune', 'ic': '', 'mr': 'https://modrinth.com/datapack/custom-vm', 'pg': 'custom-vein-miner.html',
    'desc': 'Mine entire ore veins and fell whole trees with full Fortune and Silk Touch support. Highly customizable.',
    'tagline': 'Fully configurable vein mining data pack',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Configurable max vein size (default 64 blocks)',
        'Separate toggle for ore veins vs tree felling',
        'Full Fortune and Silk Touch enchantment support',
        'Custom block whitelist/blacklist via config file',
        'Per-player toggle with persistent settings',
        'Balanced durability consumption per block mined',
    ],
    'extra': '<p>The most configurable vein miner available as a data pack. Tune every parameter — max blocks, allowed types, enchantment behavior — to fit your server rules exactly.</p>',
},
{
    'id': 'automatic-smelt-tools', 'title': 'Automatic Smelt Tools', 'type': 'datapack', 'edition': 'java',
    'icon': 'construction', 'ic': 'amber', 'mr': 'https://modrinth.com/datapack/automatic-smelt-tools', 'pg': 'automatic-smelt-tools.html',
    'desc': 'Tool-based Auto Smelt — equip smelting tools and let blocks drop their smelted forms automatically.',
    'tagline': 'Craft Auto Smelt tools to smelt blocks on break',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Craftable "smelting" variants of pickaxe, axe, and shovel',
        'Equipped smelting tool auto-smelts mined blocks',
        'Works with all smeltable blocks and ores',
        'Fortune equivalent bonus on smelted drops',
        'Tools have standard durability with fire-like appearance',
        'Per-tool control — mix and match as needed',
    ],
    'extra': '<p>Rather than a blanket toggle, Auto Smelt Tools gives you craftable tools with the smelting enchantment built in. Equip the tool, mine normally, and get smelted drops automatically.</p>',
},
{
    'id': 'better-mob-heads', 'title': 'Better Mob Heads', 'type': 'datapack', 'edition': 'java',
    'icon': 'face', 'ic': '', 'mr': 'https://modrinth.com/datapack/better-mob-heads', 'pg': 'better-mob-heads.html',
    'desc': 'Gives vanilla mobs unique decorative head drops when slain, perfect for building and collecting.',
    'tagline': 'Unique decorative heads from every vanilla mob',
    'versions': '1.17 – 1.21+', 'loader': 'Vanilla (Data Pack)',
    'features': [
        'Unique head item for every vanilla mob on death',
        'Heads are decorative blocks — place them anywhere',
        'Drop rate configurable (default ~10%)',
        'Looting enchantment increases drop chance',
        'Does not interfere with existing mob drops',
        'Hundreds of unique player head textures used',
    ],
    'extra': '<p>Build a trophy room or just collect them all. Better Mob Heads gives every vanilla mob a chance to drop a unique, decorated head item using the Minecraft player head system.</p>',
},
{
    'id': 'cave-vision-bedrock', 'title': 'Cave Vision Bedrock', 'type': 'addon', 'edition': 'bedrock',
    'icon': 'remove_red_eye', 'ic': 'teal', 'mr': 'https://modrinth.com/user/quillphen', 'pg': 'cave-vision-bedrock.html',
    'desc': 'Lightweight Bedrock addon granting infinite Night Vision — explore any cave without torches or shaders.',
    'tagline': 'Permanent Night Vision for Minecraft Bedrock Edition',
    'versions': '1.20+', 'loader': 'Bedrock Addon (.mcaddon)',
    'features': [
        'Permanent Night Vision on all players',
        'Works in caves, the Nether, and the End',
        'Import with a single .mcaddon file',
        'No shaders or resource packs required',
        'Compatible with Marketplace content',
        'Works on Bedrock, Education Edition, and Realms',
    ],
    'extra': '<p>The Bedrock counterpart to Cave Vision. Import the .mcaddon file and all players get permanent night vision — ideal for survival servers and education worlds.</p>',
},
{
    'id': 'x-ray-java', 'title': 'X-RAY Java Edition', 'type': 'resourcepack', 'edition': 'java',
    'icon': 'visibility', 'ic': 'pink', 'mr': 'https://modrinth.com/user/quillphen', 'pg': 'x-ray-java.html',
    'desc': 'Makes stone blocks semi-transparent and highlights all ore types for easy mining in Java Edition.',
    'tagline': 'See through stone to find ores instantly',
    'versions': '1.17 – 1.21+', 'loader': 'Resource Pack (OptiFine required)',
    'features': [
        'Stone, dirt, and filler blocks rendered transparent',
        'All ore types highlighted with bright colours',
        'Unique colour per ore for instant identification',
        'Configurable transparency level',
        'Works with OptiFine custom textures',
        'For singleplayer or approved servers only',
    ],
    'extra': '<p>A resource pack that makes filler blocks transparent and all ores glow brightly. Intended for creative worlds, personal singleplayer sessions, and mining practice.</p>',
},
{
    'id': 'dynamic-lighting-mcpe', 'title': 'Dynamic Lighting MCPE', 'type': 'addon', 'edition': 'bedrock',
    'icon': 'lightbulb', 'ic': 'amber', 'mr': 'https://modrinth.com/user/quillphen', 'pg': 'dynamic-lighting-mcpe.html',
    'desc': 'Real-time dynamic lighting for Bedrock — torches, lanterns, and glowstone light up when held.',
    'tagline': 'Held light sources actually illuminate Bedrock worlds',
    'versions': '1.20+', 'loader': 'Bedrock Addon (.mcaddon)',
    'features': [
        'Dynamic light emitted from held torches and lanterns',
        'Glowstone, sea lanterns, and glow berries supported',
        'Works without Render Dragon shaders',
        'Compatible with Realm and local worlds',
        'No RTX required',
        'Lightweight behavior pack — no performance issues',
    ],
    'extra': '<p>Bring dynamic lighting to Bedrock without needing RTX. Import the addon and held torches, lanterns, and other light items will actually illuminate the blocks around you.</p>',
},
]

# ─── PAGE GENERATOR ───────────────────────────────────────────────────────────

def chip(edition, ptype):
    ed_label = EDITION_LABELS.get(edition, edition)
    ty_label  = TYPE_LABELS.get(ptype, ptype)
    return (f'<span class="chip chip-{edition}">{ed_label}</span>'
            f'<span class="chip chip-{ptype}">{ty_label}</span>')

def icon_class(ic):
    return f'proj-hero-ico {ic}'.strip()

def build_page(p):
    title    = p['title']
    desc     = p['desc']
    tagline  = p['tagline']
    pg_url   = f"https://quillphen.netlify.app/{p['pg']}"
    ed_label = EDITION_LABELS.get(p['edition'], p['edition'])
    ty_label = TYPE_LABELS.get(p['type'], p['type'])
    versions = p['versions']
    loader   = p['loader']
    mr_url   = p['mr']
    icon     = p['icon']
    ic       = p['ic']
    extra    = p.get('extra', '')
    features = p.get('features', [])

    feat_items = '\n'.join(f'<li>{f}</li>' for f in features)

    ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": title,
        "description": desc,
        "url": pg_url,
        "applicationCategory": "GameApplication",
        "operatingSystem": f"Minecraft {ed_label}",
        "author": {"@type": "Person", "name": "QuillPhen",
                   "url": "https://modrinth.com/user/quillphen"},
        "downloadUrl": mr_url,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }
    import json
    ld_json = json.dumps(ld, separators=(',', ':'))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} – {tagline} | QuillPhen</title>
  <meta name="description" content="{desc} By QuillPhen on Modrinth.">
  <meta name="author" content="QuillPhen">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{pg_url}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{pg_url}">
  <meta property="og:title" content="{title} — {tagline} | QuillPhen">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">
  <meta property="og:site_name" content="QuillPhen">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} — {tagline} | QuillPhen">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">
  <meta name="theme-color" content="#006E1C">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="manifest" href="manifest.json">
  <link rel="preload" href="styles.css" as="style">
  <link rel="stylesheet" href="styles.css">
  <link rel="dns-prefetch" href="//fonts.googleapis.com">
  <script type="application/ld+json">{ld_json}</script>
</head>
<body>
{TOPBAR}
<main>
  <div class="page-wrap">
    <a href="index.html" class="back-btn">
      <span class="msrnd" style="font-size:18px">arrow_back</span>All Projects
    </a>

    <div class="proj-hero">
      <div class="{icon_class(ic)}"><span class="msrnd">{icon}</span></div>
      <h1>{title}</h1>
      <p class="sub">{tagline}</p>
      <div class="proj-hero-chips">{chip(p['edition'], p['type'])}</div>
    </div>

    <div class="dl-section">
      <h2>Download</h2>
      <p>Free on Modrinth — open-source and community supported</p>
      <div class="dl-btns">
        <a href="{mr_url}" target="_blank" rel="noopener" class="dl-btn p">
          {MDR_SVG}&nbsp;Get on Modrinth
        </a>
        <a href="index.html" class="dl-btn s">Browse All Projects</a>
      </div>
    </div>

    <div class="card-section">
      <h2><span class="msrnd">info</span>Description</h2>
      <p>{desc}</p>
      {extra}
    </div>

    <div class="card-section">
      <h2><span class="msrnd">star</span>Key Features</h2>
      <ul class="feat-list">
{feat_items}
      </ul>
    </div>

    <div class="card-section">
      <h2><span class="msrnd">settings</span>Compatibility</h2>
      <table class="specs-table">
        <tr><th>Edition</th><td>{ed_label}</td></tr>
        <tr><th>Type</th><td>{ty_label}</td></tr>
        <tr><th>Game Versions</th><td>{versions}</td></tr>
        <tr><th>Loader</th><td>{loader}</td></tr>
        <tr><th>License</th><td>MIT</td></tr>
        <tr><th>Author</th><td>QuillPhen</td></tr>
      </table>
    </div>

    <div class="dl-section" style="margin-top:1rem">
      <h2>Ready to install?</h2>
      <p>Download for free and drop it into your Minecraft world</p>
      <div class="dl-btns">
        <a href="{mr_url}" target="_blank" rel="noopener" class="dl-btn p">
          {MDR_SVG}&nbsp;Download from Modrinth
        </a>
      </div>
    </div>
  </div>
</main>
{FOOTER}
{PAGE_JS}
</body>
</html>"""

# ─── FIX INDEX.HTML ───────────────────────────────────────────────────────────

def fix_index():
    idx_path = os.path.join(BASE, 'index.html')
    with open(idx_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove ad-top banner slot
    html = re.sub(
        r'\s*<div class="ad-slot ad-banner container"[^>]*>.*?</div>\s*\n',
        '\n', html, flags=re.DOTALL)

    # Remove mid-page ad strip
    html = re.sub(
        r'\s*<div class="ad-slot ad-strip"[^>]*>.*?</div>\s*\n',
        '\n', html, flags=re.DOTALL)

    # Remove interstitial dialog
    html = re.sub(
        r'\s*<div class="interstitial"[^>]*>.*?</div>\s*\n',
        '\n', html, flags=re.DOTALL)

    # Remove profitableratecpm script tag
    html = re.sub(
        r'\s*<script[^>]*profitableratecpm[^>]*></script>\s*\n',
        '\n', html, flags=re.DOTALL)

    # Remove showInterstitial / closeInterstitial functions and their event listeners
    html = re.sub(
        r'\nfunction showInterstitial\(html\)\{.*?closeInterstitial\(\);\}\)\;\n',
        '\n', html, flags=re.DOTALL)

    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Fixed: index.html")

# ─── FIX STYLES.CSS ──────────────────────────────────────────────────────────

def fix_css():
    css_path = os.path.join(BASE, 'styles.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # Remove ad slot block
    css = re.sub(
        r'/\* ── Ad Slots .*?\*/\n\.ad-slot \{.*?\}',
        '', css, flags=re.DOTALL)

    # Remove each ad rule
    for rule in ['.ad-banner', '.ad-banner-sm', '.ad-rect', '.ad-strip']:
        css = re.sub(
            re.escape(rule) + r'\s*\{[^}]*\}',
            '', css, flags=re.DOTALL)

    # Remove interstitial block
    css = re.sub(
        r'/\* Interstitial \*/\n\.interstitial \{.*?\.interstitial-body \{[^}]*\}',
        '', css, flags=re.DOTALL)

    # Clean up consecutive blank lines
    css = re.sub(r'\n{3,}', '\n\n', css)

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"  Fixed: styles.css")

# ─── GENERATE / OVERWRITE ALL PROJECT PAGES ──────────────────────────────────

def gen_pages():
    for p in PROJECTS:
        content = build_page(p)
        path = os.path.join(BASE, p['pg'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        status = "Updated" if os.path.exists(path) else "Created"
        print(f"  {status}: {p['pg']}")

# ─── UPDATE SITEMAP ───────────────────────────────────────────────────────────

def update_sitemap():
    pages = [('index.html', '1.0', 'weekly')]
    for p in PROJECTS:
        pages.append((p['pg'], '0.8', 'monthly'))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pg, pri, freq in pages:
        url = f"https://quillphen.netlify.app/{pg}"
        lines.append(f"""  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""")
    lines.append('</urlset>')

    path = os.path.join(BASE, 'sitemap.xml')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"  Updated: sitemap.xml ({len(pages)} URLs)")

# ─── MAIN ─────────────────────────────────────────────────────────────────────

print("QuillPhen site fixer")
print("=" * 40)
print("Fixing index.html and styles.css...")
fix_index()
fix_css()
print("Generating project pages...")
gen_pages()
print("Updating sitemap...")
update_sitemap()
print("=" * 40)
print("Done!")

