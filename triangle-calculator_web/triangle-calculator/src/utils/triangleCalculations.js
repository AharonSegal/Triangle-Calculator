import { sin, cos, acos, pi, sqrt } from 'mathjs';

function radians(degrees) { return degrees * (pi / 180); }
function degrees(radians) { return radians * (180 / pi); }

function aaas(D, E, F, f) {
  const d = f * sin(D) / sin(F);
  const e = f * sin(E) / sin(F);
  return [d, e, f, D, E, F];
}

function sss(d, e, f) {
  if (!(d + e > f && e + f > d && f + d > e)) {
    throw new Error("Invalid triangle: sum of two sides must be greater than the third side");
  }
  const F = acos((d**2 + e**2 - f**2) / (2 * d * e));
  const E = acos((d**2 + f**2 - e**2) / (2 * d * f));
  const D = pi - F - E;
  return [d, e, f, D, E, F];
}

function sas(d, e, F) {
  const f = sqrt(d**2 + e**2 - 2 * d * e * cos(F));
  return sss(d, e, f);
}

function area(a, b, c) {
  const s = (a + b + c) / 2;
  return sqrt(s * (s - a) * (s - b) * (s - c));
}

function perimeter(a, b, c) {
  return a + b + c;
}

export function calculateTriangle(a, b, c, A, B, C) {
  const sides = [a, b, c].filter(side => side !== null && side !== '');
  const angles = [A, B, C].filter(angle => angle !== null && angle !== '');

  if (sides.length + angles.length !== 3) {
    throw new Error("Must provide exactly 3 inputs");
  }
  if (sides.length === 0) {
    throw new Error("Must provide at least 1 side length");
  }

  [A, B, C] = [A, B, C].map(angle => angle ? radians(parseFloat(angle)) : null);

  let result;
  if (sides.length === 3) {
    result = sss(a, b, c);
  } else if (sides.length === 2 && angles.length === 1) {
    if (A !== null) result = sas(b, c, A);
    else if (B !== null) result = sas(c, a, B);
    else result = sas(a, b, C);
  } else if (sides.length === 1 && angles.length === 2) {
    let knownSide, knownAngle1, knownAngle2;
    if (a !== null) [knownSide, knownAngle1, knownAngle2] = [a, B, C];
    else if (b !== null) [knownSide, knownAngle1, knownAngle2] = [b, C, A];
    else [knownSide, knownAngle1, knownAngle2] = [c, A, B];

    const unknownAngle = pi - knownAngle1 - knownAngle2;
    result = aaas(knownAngle1, knownAngle2, unknownAngle, knownSide);
  } else {
    throw new Error("Invalid combination of inputs");
  }

  result[3] = degrees(result[3]);
  result[4] = degrees(result[4]);
  result[5] = degrees(result[5]);

  const [side1, side2, side3, angle1, angle2, angle3] = result;

  return {
    side1: side1.toFixed(2),
    side2: side2.toFixed(2),
    side3: side3.toFixed(2),
    angle1: angle1.toFixed(2),
    angle2: angle2.toFixed(2),
    angle3: angle3.toFixed(2),
    area: area(side1, side2, side3).toFixed(2),
    perimeter: perimeter(side1, side2, side3).toFixed(2)
  };
}