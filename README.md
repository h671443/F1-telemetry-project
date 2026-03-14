# F1-telemetry-project
Project Aimed to gather F1 telemetry data


struct PacketHeader
    {
    uint16 m_packetFormat; // 2025
    uint8 m_gameYear; // Game year - last two digits e.g. 25
    uint8 m_gameMajorVersion; // Game major version - "X.00"
    uint8 m_gameMinorVersion; // Game minor version - "1.XX"
    uint8 m_packetVersion; // Version of this packet type, all start from 1
    uint8 m_packetId; // Identifier for the packet type, see below
    uint64 m_sessionUID; // Unique identifier for the session
    float m_sessionTime; // Session timestamp
    uint32 m_frameIdentifier; // Identifier for the frame the data was retrieved on
    uint32 m_overallFrameIdentifier; // Overall identifier for the frame the data was retrieved
    // on, doesn't go back after flashbacks
    uint8 m_playerCarIndex; // Index of player's car in the array
    uint8 m_secondaryPlayerCarIndex; // Index of secondary player's car in the array (splitscreen)
    // 255 if no second player
    };




GRAFANA

install GRAFANA ALLOY:
Option 1: Grafana Alloy (recommended)
Alloy is Grafana's telemetry collector that can scrape and forward metrics.

    Install Alloy on your machine — get it at grafana.com/docs/alloy
    Configure it to scrape your Prometheus targets and remote_write to Grafana Cloud
    Your Cloud credentials (endpoint + API key) are in Connections → Data sources → Prometheus
    - https://grafana.com/docs/alloy/latest/set-up/install/docker/
    - https://grafana.com/docs/alloy/latest/set-up/install/linux/
    
