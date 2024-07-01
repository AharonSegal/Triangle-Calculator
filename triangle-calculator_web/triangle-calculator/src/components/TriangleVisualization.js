import React, { useEffect, useState } from 'react';
import './TriangleVisualization.css';

const TriangleVisualization = ({ result }) => {
  const [dashOffset, setDashOffset] = useState(1000);

  useEffect(() => {
    const timer = setTimeout(() => setDashOffset(0), 100);
    return () => clearTimeout(timer);
  }, [result]);

  if (!result) return null;

  const { side1, side2, side3, angle1, angle2, angle3 } = result;

  // Convert strings to numbers and provide default values
  const s1 = Number(side1) || 0;
  const s2 = Number(side2) || 0;
  const s3 = Number(side3) || 0;
  const a1 = Number(angle1) || 0;
  const a2 = Number(angle2) || 0;
  const a3 = Number(angle3) || 0;

  // Calculate triangle coordinates (increased scale)
  const scale = 150 / Math.max(s1, s2, s3);
  const a = s1 * scale;
  const c = s3 * scale;

  const angleC = a3 * Math.PI / 180;
  
  const x1 = 0;
  const y1 = 0;
  const x2 = a;
  const y2 = 0;
  const x3 = c * Math.cos(angleC);
  const y3 = c * Math.sin(angleC);

  // Calculate the bounding box
  const minX = Math.min(x1, x2, x3);
  const minY = Math.min(y1, y2, y3);
  const maxX = Math.max(x1, x2, x3);
  const maxY = Math.max(y1, y2, y3);
  const width = maxX - minX;
  const height = maxY - minY;

  // Add padding
  const padding = 60; // Increased padding
  const viewBoxWidth = width + padding * 2;
  const viewBoxHeight = height + padding * 2;

  // Shift the triangle down and right
  const shiftX = -minX + padding;
  const shiftY = -minY + padding;

  // SVG path for the triangle
  const path = `M${x1 + shiftX},${y1 + shiftY} L${x2 + shiftX},${y2 + shiftY} L${x3 + shiftX},${y3 + shiftY} Z`;

  // Pastel/ancient color scheme
  const colors = {
    side1: '#D2B48C', // tan
    side2: '#DEB887', // burlywood
    side3: '#F4A460', // sandy brown
    angle1: '#98FB98', // pale green
    angle2: '#DDA0DD', // plum
    angle3: '#F0E68C'  // khaki
  };

  return (
    <div className="triangle-visualization">
      <svg viewBox={`0 0 ${viewBoxWidth} ${viewBoxHeight}`}>
        <path 
          d={path} 
          fill="none" 
          stroke="#8B4513" // saddlebrown
          strokeWidth="1" // Reduced from 2 to 1
          strokeDasharray={1000}
          strokeDashoffset={dashOffset}
          style={{ transition: 'stroke-dashoffset 1s ease-out' }}
        />
        
        {/* Side labels */}
        <text x={(x1 + x2) / 2 + shiftX} y={y1 + shiftY - 15} textAnchor="middle" fill={colors.side1}>{s1.toFixed(2)}</text>
        <text x={(x2 + x3) / 2 + shiftX + 15} y={(y2 + y3) / 2 + shiftY} textAnchor="start" fill={colors.side3}>{s3.toFixed(2)}</text>
        <text x={(x1 + x3) / 2 + shiftX - 15} y={(y1 + y3) / 2 + shiftY} textAnchor="end" fill={colors.side2}>{s2.toFixed(2)}</text>
        
        {/* Angle labels */}
        <text x={x1 + shiftX - 15} y={y1 + shiftY + 25} textAnchor="end" fill={colors.angle3}>{a3.toFixed(2)}°</text>
        <text x={x2 + shiftX + 15} y={y2 + shiftY + 25} textAnchor="start" fill={colors.angle2}>{a2.toFixed(2)}°</text>
        <text x={x3 + shiftX} y={y3 + shiftY - 20} textAnchor="middle" fill={colors.angle1}>{a1.toFixed(2)}°</text>
      
        
      
      
      </svg>
    </div>
  );
};

export default TriangleVisualization;