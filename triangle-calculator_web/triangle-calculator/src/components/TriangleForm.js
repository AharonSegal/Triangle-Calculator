import React, { useState, useEffect } from 'react';
import './TriangleForm.css';

const colors = {
  side1: '#D2B48C', // tan
  side2: '#DEB887', // burlywood
  side3: '#F4A460', // sandy brown
  angle1: '#98FB98', // pale green
  angle2: '#DDA0DD', // plum
  angle3: '#F0E68C'  // khaki
};

function TriangleForm({ onCalculate, result }) {
  const [formData, setFormData] = useState({
    side1: '', side2: '', side3: '',
    angle1: '', angle2: '', angle3: ''
  });

  useEffect(() => {
    if (result && !result.error) {
      setFormData({
        side1: formatValue(result.side1),
        side2: formatValue(result.side3),
        side3: formatValue(result.side2),
        angle1: formatValue(result.angle3),
        angle2: formatValue(result.angle2),
        angle3: formatValue(result.angle1)
      });
    }
  }, [result]);

  const formatValue = (value) => {
    if (typeof value === 'number') {
      return value.toFixed(2);
    } else if (typeof value === 'string') {
      const num = parseFloat(value);
      return isNaN(num) ? value : num.toFixed(2);
    }
    return value;
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onCalculate(formData);
  };

  const handleClear = () => {
    setFormData({
      side1: '', side2: '', side3: '',
      angle1: '', angle2: '', angle3: ''
    });
  };

  return (
    <form onSubmit={handleSubmit} className="triangle-form">
      <div className="triangle">
        <svg viewBox="0 0 300 260" className="triangle-svg">
          <path d="M150,10 L10,250 L290,250 Z" fill="none" stroke="#8B4513" strokeWidth="2" />
        </svg>
        {Object.entries(formData).map(([key, value]) => (
          <div key={key} className={`input-group ${key}`}>
            <input 
              type="text" 
              name={key} 
              value={value} 
              onChange={handleChange} 
              placeholder={key.charAt(0).toUpperCase() + key.slice(1)}
              style={{ borderColor: colors[key] }}
            />
          </div>
        ))}
        {result && !result.error && (
          <div className="triangle-info">
            <p>Area: {result.area}</p>
            <p>Perimeter: {result.perimeter}</p>
          </div>
        )}
      </div>
      <div className="button-group">
        <button type="submit">Calculate</button>
        <button type="button" onClick={handleClear}>Clear</button>
      </div>
    </form>
  );
}

export default TriangleForm;