const devices = {
  sensor_altura: "eff7e5ff-f872-4f10-a631-ae54ebd62d29",
  esteira: "c8fc1615-b429-47bd-8293-911b534a232c",
  sensor_rampa1: "82845a6a-3981-4f20-93bd-884a59fc92e9",
  sensor_rampa2: "64fcf23d-861b-45f4-82b3-6a2774d75808",
  sensor_capacitivo: "070b84ea-331d-4c14-b8dc-41b84cc3cf10",
  sensor_indutivo: "920d24b2-7159-4595-a278-2809223d8de5",
  sensor_final_esteira: "f863331b-90d2-4f3c-809b-349cfd12c7cc",
  atuador1: "985c1c59-d52a-458a-80ae-f46435d5491a",
  atuador2: "b52eef9a-9a14-490f-9718-cdc5bb092d0c"
};

function randomDateWithinMonth() {
    const now = new Date();
    const past = new Date(now);
    past.setMonth(now.getMonth() - 1);
    const randTime = past.getTime() + Math.random() * (now.getTime() - past.getTime());
    return new Date(randTime);
}

// Avança segundos na mesma data base
function addSecondsToDate(baseDate, seconds) {
    return new Date(baseDate.getTime() + seconds * 1000);
}

// Aleatoriedade simples
function chance(prob) {
    return Math.random() < prob;
}

// 1. Escolhe o tipo da peça
const tipo = Math.random() < 0.5 ? "plástico" : "metálico";

// 2. Escolhe se será refugo (20% de chance)
const isRefugo = chance(0.2);

// 3. Gera a data base aleatória
const baseDate = randomDateWithinMonth();

// 4. Gera sequência de eventos
let events = [];
let step = 0;

events.push({
    device_id: devices.esteira,
    state: true,
    timestamp: addSecondsToDate(baseDate, step++).toISOString()
});

if (isRefugo) {
    events.push({
        device_id: devices.sensor_altura,
        state: true,
        timestamp: addSecondsToDate(baseDate, step++).toISOString()
    });
    events.push({
        device_id: devices.sensor_final_esteira,
        state: true,
        timestamp: addSecondsToDate(baseDate, step++).toISOString()
    });
} else {
    if (tipo === "plástico") {
        events.push({
            device_id: devices.sensor_capacitivo,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
        events.push({
            device_id: devices.sensor_rampa1,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
        events.push({
            device_id: devices.atuador1,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
    } else {
        events.push({
            device_id: devices.sensor_indutivo,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
        events.push({
            device_id: devices.sensor_rampa2,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
        events.push({
            device_id: devices.atuador2,
            state: true,
            timestamp: addSecondsToDate(baseDate, step++).toISOString()
        });
    }
}

// Retorna o primeiro evento e guarda os outros
msg.payload = events.shift();
msg.remaining = events;
return msg;