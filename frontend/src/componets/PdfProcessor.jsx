import React, { useState } from "react";
import axios from "axios";
import ExtractedDataList from "./ExtractedDataList";

const PdfProcessor = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("pdf_file", file);
    try {
      const response = await axios.post(
        "https://build-drf-j3hrmc2g9-pdf-projects.vercel.app/process_pdf/",
        formData
      );
      setResponse(response.data);
    } catch (error) {
      console.error("Error processing PDF:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button
          type="submit"
          className=""
          style={{ color: "blue", backgroundColor: "white" }}
        >
          Process PDF
        </button>
      </form>

      <ExtractedDataList></ExtractedDataList>
    </div>
  );
};

export default PdfProcessor;
