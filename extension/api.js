// api.js
// Purpose: fetch wrapper for backend calls. Returns raw ArrayBuffer/JSON — no DOM APIs.

// async function postTailorRequest(payload)
//   - POST to {BACKEND_URL}/api/v1/tailor with JSON body
//   - On !response.ok -> parse error JSON, throw Error(detail)
//   - On success -> return response.arrayBuffer() (binary .docx)

// async function postExtractRequest(fileFormData)
//   - POST multipart/form-data to {BACKEND_URL}/api/v1/extract
//   - Returns parsed JSON { resume_text, extraction_confidence }
//   - Throws on non-ok response same pattern as postTailorRequest
