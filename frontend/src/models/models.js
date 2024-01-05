export const Album = {
    AlbumID: {
        type: Number,
    },
    Title: {
        type: String,
    },
    Publishing_Date: {
        type: String,
    },
    Cover: {
        type: String,
    },
    ArtistID: {
        type: Number,
    },
    GenreID: {
        type: Number,
    },
};

export const Artist = {
    ArtistID: {
        type: Number,
    },
    Full_Name: {
        type: String,
    },
    Country: {
        type: String,
    },
    Photo: {
        type: String,
    },
    GenreID: {
        type: Number,
    },
};

export const Genre = {
    GenreID: {
        type: Number,
    },
    Name: {
        type: String,
    }
}

export const Playlist = {
    PlaylistID: {
        type: Number,
    },
    Name: {
        type: String,
    },
    UserID: {
        type: Number,
    },
    SongID: {
        type: Number,
    },
};

export const Song = {
    Title: {
        type: String,
    },
    Upload_Date: {
        type: String,
    },
    Song_Filepath: {
        type: String,
    },
    Description: {
        type: String,
    },
    ArtistID: {
        type: Number,
    },
    AlbumID: {
        type: Number,
    },
};

export const User = {
    UserID: {
        type: Number,
    },
    Name: {
        type: String,
    },
    Surname: {
        type: String,
    },
    Username: {
        type: String,
    },
    Password: {
        type: String,
    },
    Email: {
        type: String,
    },
    Registration_Date: {
        type: String,
    },
};