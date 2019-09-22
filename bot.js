const Discord = require('discord.js')
const client = new Discord.Client()

client.login("")

client.on('message', message => {
  // Voice only works in guilds, if the message does not come from a guild, we ignore it
  if (!message.guild) return;

  if (message.content === '/join') {
    // Only try to join the sender's voice channel if they are in one themselves
    if (message.member.voiceChannel) {
      message.member.voiceChannel.join()
        .then(connection => { // Connection is an instance of VoiceConnection
          message.reply('Avanti!');
          const dispatcher = connection.playFile('C:/Users/Eduardo/Desktop/TóFerreiraBot/voice.mp3');
        })
        .catch(console.log);
    } else {
      message.reply('You need to join a voice channel first!');
    }
  }

  if (message.content === "/count") {
    message.channel.messages.fetch({around: "207090194006933505", limit: 10})
    .then(messages => {
      messages.first().edit("This fetched message was edited");
    })
  };
});

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})