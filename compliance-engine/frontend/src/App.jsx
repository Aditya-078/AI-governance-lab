import { useEffect, useState } from "react";
import { getHealth } from "./api/api";

function App() {

  const [backend, setBackend] = useState(null);

  useEffect(() => {

    getHealth()
      .then(data => setBackend(data))
      .catch(console.error);

  }, []);

  return (

    <div style={{ padding: "40px" }}>

      <h1>Enterprise AI Governance</h1>

      <h2>Compliance Engine</h2>

      {backend ? (

        <>
          <h3>{backend.status}</h3>

          <p>
            <strong>Project:</strong> {backend.project}
          </p>

          <p>
            <strong>Version:</strong> {backend.version}
          </p>

        </>

      ) : (

        <p>Connecting to backend...</p>

      )}

    </div>

  );

}

export default App;