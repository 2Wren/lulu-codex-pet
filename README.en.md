<div align="center">

# Codex Capybara Lulu Pet

**[简体中文](./README.md) · English**

A Capybara Lulu (水豚噜噜) desktop pet for Codex

</div>

## Animation Preview

<div align="center">

<table>
  <tr>
    <td align="center"><strong>Idle</strong><br /><img src="./lulu/previews/idle.png" width="160" alt="Lulu idle animation" /><br /><code>idle</code> · 6 frames</td>
    <td align="center"><strong>Waving</strong><br /><img src="./lulu/previews/waving.png" width="160" alt="Lulu waving animation" /><br /><code>waving</code> · 4 frames</td>
    <td align="center"><strong>Jumping</strong><br /><img src="./lulu/previews/jumping.png" width="160" alt="Lulu jumping animation" /><br /><code>jumping</code> · 5 frames</td>
  </tr>
  <tr>
    <td align="center"><strong>Move left</strong><br /><img src="./lulu/previews/running-left.png" width="160" alt="Lulu moving left" /><br /><code>running-left</code> · 8 frames</td>
    <td align="center"><strong>Working</strong><br /><img src="./lulu/previews/running.png" width="160" alt="Lulu working animation" /><br /><code>running</code> · 6 frames</td>
    <td align="center"><strong>Move right</strong><br /><img src="./lulu/previews/running-right.png" width="160" alt="Lulu moving right" /><br /><code>running-right</code> · 8 frames</td>
  </tr>
  <tr>
    <td align="center"><strong>Waiting for input</strong><br /><img src="./lulu/previews/waiting.png" width="160" alt="Lulu waiting animation" /><br /><code>waiting</code> · 6 frames</td>
    <td align="center"><strong>Ready for review</strong><br /><img src="./lulu/previews/review.png" width="160" alt="Lulu review animation" /><br /><code>review</code> · 6 frames</td>
    <td align="center"><strong>Failed or blocked</strong><br /><img src="./lulu/previews/failed.png" width="160" alt="Lulu failed animation" /><br /><code>failed</code> · 8 frames</td>
  </tr>
</table>

### Look Directions

<p align="center">
  <img src="./lulu/previews/look-directions.png" width="192" alt="Lulu's 16 look directions" /><br />
  <code>look directions</code> · 16 directions
</p>

</div>

## Installation

> [!NOTE]
> Pets are stored in your ChatGPT account and shared between the Codex desktop app and ChatGPT: install Lulu in one and you can pick it in the other.

### Option 1: Ask Codex to install it with the Pets plugin (recommended)

Tell Codex:

> Use the Pets plugin to install Capybara Lulu: download `lulu/spritesheet.webp` from <https://github.com/2Wren/lulu-codex-pet>. It is a finished, validated sprite sheet, so upload it as is without regenerating or editing it. Name it "水豚噜噜", use the `description` from `lulu/pet.json`, and select it after creating it.

### Option 2: Copy it into the pets folder

1. Clone the repository:

   ```bash
   git clone https://github.com/2Wren/lulu-codex-pet.git
   ```

2. Open the Codex App and go to **Settings → Pets → Custom pets → Open folder**.
3. Copy the `lulu` folder from the repository into the opened directory.
4. Return to the Codex App, click **Refresh**, and select Capybara Lulu.

Command line (macOS / Linux):

```bash
git clone https://github.com/2Wren/lulu-codex-pet.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/pets/lulu"
cp -R lulu-codex-pet/lulu/. "${CODEX_HOME:-$HOME/.codex}/pets/lulu/"
```

Command line (Windows PowerShell):

```powershell
git clone https://github.com/2Wren/lulu-codex-pet.git
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$petDir = Join-Path $codexHome "pets\lulu"
New-Item -ItemType Directory -Force $petDir | Out-Null
Copy-Item ".\lulu-codex-pet\lulu\*" $petDir -Recurse -Force
```

> [!TIP]
> The first time Codex reads this folder, it uploads Lulu to your account and shows that copy from then on. Later edits to the files in the folder are not synced; see the next section to update.

### Option 3: ChatGPT Web only

Upload [`lulu/spritesheet.webp`](./lulu/spritesheet.webp) under **Settings → Personalization → Pet → Upload pet**. The upload dialog accepts `1536 × 2288` v2 sprite sheets.

## Updating

After pulling the latest version of the repository, tell Codex:

> Use the Pets plugin to replace the sprite sheet of my "水豚噜噜" pet with `<repo path>/lulu/spritesheet.webp`. Use this file as is without regenerating or editing it, and keep the same pet ID.

## File Structure

```text
lulu/
├── pet.json
├── spritesheet.webp
└── previews/
    ├── idle.png
    └── …
```

- `pet.json`: pet metadata (name, description)
- `spritesheet.webp`: v2 animation sprite sheet (`1536 × 2288`, 8 columns × 11 rows, 73 frames), used by both the Codex desktop app and ChatGPT
- `previews/`: README preview images; not needed at runtime

## Regenerating

Lulu's sprite sheet was originally generated with the built-in Codex `$hatch-pet` skill. The official workflow is now the Codex **Pets plugin** (`create-pet` / `update-pet`), which uses the same format. `scripts/release.py` validates the sprite sheet against the Pets plugin's rules and exports the README previews:

```bash
python3 scripts/release.py --source <folder containing pet.json and spritesheet.webp>
```

## Copyright

The Capybara Lulu (水豚噜噜) character and related rights belong to its original creator / rights holder. This is an unofficial fan project for personal, non-commercial use only; if the rights holder objects, please get in touch and it will be removed.

The scripts and documentation in this repository are licensed under the [MIT License](LICENSE); the character artwork is not covered by the MIT License.
