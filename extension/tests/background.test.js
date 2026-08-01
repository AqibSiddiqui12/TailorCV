// background.test.js
// Purpose: Jest tests for background.js logic.

// test('bufferToDataUrl produces correct base64 data URL')
//   - Feeds a known ArrayBuffer, asserts output matches expected data:...;base64,... string

// test('TAILOR_RESUME handler returns {ok:true, downloadId} on success')
//   - Mocks api.postTailorRequest to resolve with a fake ArrayBuffer
//   - Mocks chrome.downloads.download to call back with a fake downloadId
//   - Asserts sendResponse called with {ok:true, downloadId}

// test('TAILOR_RESUME handler returns {ok:false, error} on fetch failure')
//   - Mocks api.postTailorRequest to reject
//   - Asserts sendResponse called with {ok:false, error: <message>}
