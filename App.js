import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';


const SOCKET_URL = process.env.REACT_APP_SOCKET_URL || 'http://localhost:4000';
const socket = io(SOCKET_URL);


function App(){
const [events, setEvents] = useState([]);


useEffect(()=>{
socket.on('counts', (d)=> setEvents(prev=>[{type:'counts',d,ts:Date.now()},...prev].slice(0,50)));
socket.on('actuation', (d)=> setEvents(prev=>[{type:'actuation',d,ts:Date.now()},...prev].slice(0,50)));
socket.on('emergency', (d)=> setEvents(prev=>[{type:'emergency',d,ts:Date.now()},...prev].slice(0,50)));
return () => { socket.off('counts'); socket.off('actuation'); socket.off('emergency'); }
},[]);


async function triggerEmergency(){
await fetch((process.env.REACT_APP_API_URL || 'http://localhost:4000') + '/api/emergency', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({direction:'left'})});
alert('Emergency sent');
}


return (
<div style={{padding:20,fontFamily:'Arial'}}>
<h2>Smart Traffic Dashboard</h2>
<button onClick={triggerEmergency}>Send Manual Emergency (Left)</button>
<div style={{marginTop:20}}>
{events.map((e, i)=> (
<div key={i} style={{border:'1px solid #ddd',padding:8,margin:6}}>
<b>{e.type}</b>: <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(e.d, null, 2)}</pre>
</div>
))}
</div>
</div>
);
}


export default App;