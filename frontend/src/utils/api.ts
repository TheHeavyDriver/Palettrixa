export async function extractPalette(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(
    "https://palettrixa.onrender.com/extract-palette",
    {
      method: "POST",
      body: formData,
    }
  );

  const text = await response.text();

  console.log("RAW RESPONSE:", text);

  if (!response.ok) {
    console.error("Backend error:", text);
    throw new Error(text);
  }

  const data = JSON.parse(text);

  if (Array.isArray(data)) {
    return { colors: data };
  }

  return data;
}