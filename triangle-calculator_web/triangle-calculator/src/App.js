import React, { useState } from 'react';
import TriangleForm from './components/TriangleForm';
import TriangleVisualization from './components/TriangleVisualization';
import { calculateTriangle } from './utils/triangleCalculations';
import './App.css';

function App() {
  const [result, setResult] = useState(null);

  const handleCalculate = (formData) => {
    try {
      const { side1, side2, side3, angle1, angle2, angle3 } = formData;
      const calculatedResult = calculateTriangle(
        side1 ? parseFloat(side1) : null,
        side2 ? parseFloat(side2) : null,
        side3 ? parseFloat(side3) : null,
        angle1 ? parseFloat(angle1) : null,
        angle2 ? parseFloat(angle2) : null,
        angle3 ? parseFloat(angle3) : null
      );
      setResult(calculatedResult);
    } catch (error) {
      setResult({ error: error.message });
    }
  };

  return (
    <div className="App">
      <h1>Triangle Calculator</h1>
      <TriangleForm onCalculate={handleCalculate} result={result} />
      {result && !result.error && <TriangleVisualization result={result} />}
      {result && result.error && (
        <div className="error">
          <p>{result.error}</p>
        </div>
      )}
    </div>
  );
}

export default App;