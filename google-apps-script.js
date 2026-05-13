const SPREADSHEET_ID = "1i8lRUlj0sW1D-QP5k2vTD-din8PFX-b5jCk6ZL0lG2U";
const SHEET_GID = 0;

function doGet() {
  const file = SpreadsheetApp.openById(SPREADSHEET_ID);
  const sheet = getSheetByGid_(file, SHEET_GID);
  const values = sheet.getDataRange().getDisplayValues();
  const csv = values.map(rowToCsv_).join("\r\n");

  return ContentService
    .createTextOutput(csv)
    .setMimeType(ContentService.MimeType.CSV);
}

function getSheetByGid_(file, gid) {
  const sheets = file.getSheets();
  for (const sheet of sheets) {
    if (sheet.getSheetId() === gid) {
      return sheet;
    }
  }
  return sheets[0];
}

function rowToCsv_(row) {
  return row.map(value => {
    const text = String(value == null ? "" : value);
    if (/[",\r\n]/.test(text)) {
      return `"${text.replace(/"/g, '""')}"`;
    }
    return text;
  }).join(",");
}
