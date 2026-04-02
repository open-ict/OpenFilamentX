export default function App() {
  const sample = {
    temperature: 210,
    diameter: 1.75,
    speed: 8,
    quality: "good",
  };

  return (
    <main style={{ fontFamily: "Arial, sans-serif", padding: 24 }}>
      <h1>OpenFilamentX Dashboard</h1>
      <p>MVP operator view for extrusion telemetry.</p>
      <ul>
        <li>Temperature: {sample.temperature} °C</li>
        <li>Diameter: {sample.diameter} mm</li>
        <li>Speed: {sample.speed} mm/s</li>
        <li>Quality: {sample.quality}</li>
      </ul>
    </main>
  );
}
