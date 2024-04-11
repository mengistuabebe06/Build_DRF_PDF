import React, { useState, useEffect } from "react";
import "../ExtractedDataList.css";

const ExtractedDataList = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/extracted_data/");
      if (response.ok) {
        const jsonData = await response.json();
        setData(jsonData);
      } else {
        console.error("Failed to fetch data:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="extracted-data-container">
      <h1 className="title">Extracted Data List</h1>
      <table className="data-table">
        <thead>
          <tr>
            <th>Email</th>
            <th>Nouns</th>
            <th>Verbs</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.email}</td>
              <td>{item.nouns}</td>
              <td>{item.verbs}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ExtractedDataList;
