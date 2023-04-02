// 10.	Songs - CLASSES
function songs(input) {
    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }

    }
    let songs = [];
    let typeList = '';
    let songsCount = 0;
    songsCount = Number(input.shift());
    typeList = input.pop();
    // for (let i = 0; i < input.length; i++) {
    for (let item of input) {
        let [type, name, time] = item.split('_');
        songs.push(new Song(type, name, time))
    };
    let result = [];
    if (typeList=='all') {
        result = songs;
    } else {
        result = songs.filter ((song)=> song.type == typeList);
    };
    result.forEach((song)=>console.log(song.name));

}

// songs ([3,
//     'favourite_DownTown_3:14',
//     'favourite_Kiss_4:16',
//     'favourite_Smooth Criminal_4:01',
//     'favourite']
//     )

// songs([4,
//     'favourite_DownTown_3:14',
//     'listenLater_Andalouse_3:24',
//     'favourite_In To The Night_3:58',
//     'favourite_Live It Up_3:48',
//     'listenLater']
//     );

songs([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
    );