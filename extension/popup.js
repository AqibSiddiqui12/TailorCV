// popup.js
// Purpose: UI logic only. Never holds a long fetch itself — always delegates
// to background.js via chrome.runtime.sendMessage, since popups die on blur.

// async function initPopup()
//   - On popup open: calls storage.hasMasterResume() to gate the tailor button
//   - If master resume exists, calls storage.loadMasterResume() to show upload status
//   - Loads storage.loadLastTailorPrefs() to pre-fill dropdowns

// async function handlePdfUpload(file)
//   - Builds FormData from the selected file
//   - Sends {type: 'EXTRACT_RESUME', payload: formData} to background.js
//   - On success -> storage.saveMasterResume(resume_text, extraction_confidence)
//   - Shows extraction_confidence to user if low (flag potential bad parse)

// function validateJobDescription(text)
//   - Client-side min-length check (mirrors backend's min_length=50) before sending
//   - Returns boolean

// async function handleTailorClick()
//   - Validates job description via validateJobDescription()
//   - Loads master resume via storage.loadMasterResume()
//   - Reads cv_type/language from the two dropdowns
//   - Sends {type: 'TAILOR_RESUME', payload: {...}} to background.js
//   - Shows loading state while awaiting response
//   - On response.ok -> showSuccess(); else -> showError(response.error)

// function showError(message)
//   - Displays an inline error banner in the popup

// function showSuccess(message)
//   - Displays an inline success banner (e.g. "Resume tailored and downloaded!")

// function showLoadingState(isLoading)
//   - Toggles a spinner/disabled state on the "Tailor resume" button
