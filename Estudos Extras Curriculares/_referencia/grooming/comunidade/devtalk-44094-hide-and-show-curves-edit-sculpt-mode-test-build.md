---
titulo: Hide and show curves in Edit Mode and Sculpt Mode. Test Build
autor: aicedor
url: https://devtalk.blender.org/t/hide-and-show-curves-in-edit-mode-and-sculpt-mode-test-build/44094
data: 2026-01-22
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — aicedor — 2026-01-22T12:56:30.463Z

Good afternoon! I I have created code to implement the functionality of hiding curves and points for the Curves data type in Edit Mode and Sculpt Mode, and the functionality is similar to how it works for the old curve bezier data type.
You can see how it works in the video:
The user can create a Curves object, add curves to the scene, and use the Curves → Show/Hide → Hide Selected menu item to hide the curves (or use the H hotkey). The curves will be hidden.
To show the curves, we use the Curves → Show/Hide → Reveal menu item or the Alt + H hotkeys.
This functionality also works in Sculpt Mode.
image
1920×1025 100 KB
blender_MR7i376ia1
2560×1366 353 KB
Known bugs/features that are not yet implemented:
If at least one point remains unhidden in the curve, we can use Proportional Editing to move all points within the curve (the design for this will be defined later in other patches not related to hiding curves).
The name in the Reveal menu item will be expanded to Reveal Hidden, as it is now in other places in Blender.
I have only compiled Blender 5.1 for Windows (tested on Windows 11).
drive.google.com
Blender Hiding Curves test Build.7z
Google Drive file.
All code is located in the branch
aicedor/blender: The official Blender project repository. Copy for Nazir - blender - Blender Projects
for those who want to compile it for other platforms.
Related PRs with my build (3/6):
Curves: Add initial implementation to support curve hiding
Curves: Add hide attribute VBO support for curves in edit mode
Curves: add hide and reveal operators for curves in Edit Mode
Currently, only 3 of the 6 PRs related to my build are presented in Gitea. The remaining 3 PRs depend on this code and will be added later when the main commits are accepted.

---