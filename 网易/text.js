import 'APlayer/dist/APlayer.min.css';
import APlayer from 'APlayer';

 const ap = new APlayer({
    container: document.getElementById('aplayer'),
    lrcType: 2,
    audio: [[
        {
            name: 'name1',
            artist: 'artist1',
            url: 'url1.mp3',
            cover: 'cover1.jpg'
        },
        {
            name: 'name2',
            artist: 'artist2',
            url: 'url2.mp3',
            cover: 'cover2.jpg'
        }
    ]]
});