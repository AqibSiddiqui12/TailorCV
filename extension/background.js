// background.js
// Purpose: MV3 service worker — owns all long-running fetches so popup.js closing
// doesn't kill an in-flight request. Also handles docx download.

// importScripts('api.js')

// function bufferToDataUrl(buffer, mimeType)
//   - Converts ArrayBuffer -> Uint8Array -> binary string -> base64 via btoa()
//   - Returns `data:${mimeType};base64,${encoded}`
//   - No DOM APIs used (URL.createObjectURL is unreliable in service workers)

// chrome.runtime.onMessage.addListener(...)
//   - on message.type === 'EXTRACT_RESUME':
//       calls api.postExtractRequest(message.payload), sendResponse(result or error)
//   - on message.type === 'TAILOR_RESUME':
//       calls api.postTailorRequest(message.payload)
//       -> bufferToDataUrl() -> chrome.downloads.download({url, filename, saveAs:false})
//       -> sendResponse({ok, downloadId} or {ok:false, error})
//   - MUST `return true` in the listener to keep the async channel open
