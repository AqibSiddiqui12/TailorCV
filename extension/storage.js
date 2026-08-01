// storage.js
// Purpose: sole owner of chrome.storage.local reads/writes. popup.js only calls these.

// async function saveMasterResume(resumeText, extractionConfidence)
//   - Writes { resumeText, uploadedAt: new Date().toISOString(), extractionConfidence }
//     under key "masterResume" in chrome.storage.local

// async function loadMasterResume()
//   - Reads the "masterResume" key, returns the stored object or null

// async function hasMasterResume()
//   - Returns boolean — true if a masterResume entry exists
//   - Used to gate the "Tailor resume" button in the UI (Phase 1 must be done first)

// async function saveLastTailorPrefs(cvType, language)
//   - Writes { cvType, language } under "lastTailorPrefs" — UX convenience only

// async function loadLastTailorPrefs()
//   - Reads "lastTailorPrefs", returns defaults if not present
