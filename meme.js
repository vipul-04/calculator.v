const link_1='https://cloud-71tjo809m-hack-club-bot.vercel.app/0image.png'

const link_2 = 'https://cloud-7u4dgy5xr-hack-club-bot.vercel.app/0image.png'

const link_3 = 'https://cloud-kdk2xn0a7-hack-club-bot.vercel.app/0image.png'

const link_4= 'https://cloud-aqa0xnw0b-hack-club-bot.vercel.app/0image.png'

const link_5 = 
'https://cloud-l7agk1z75-hack-club-bot.vercel.app/0image.png'

const links = [link_1,link_2,link_3,link_4,link_5]

let meme_number = 0

function change_shiba(){ 

const meme = document.getElementById("meme")

meme_number += 1

if(meme_number == links.length){
  meme_number = 0
}

meme.src = links[meme_number]

} 