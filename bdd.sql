-- 1) Clientes do Canadá
SELECT FirstName || ' ' || LastName AS FullName, Email
FROM Customer
WHERE Country = 'Canada';

-- 2) Albuns e artistas
SELECT Album.Title AS AlbumName, Artist.Name AS ArtistName
FROM Album
JOIN Artist ON Album.ArtistId = Artist.ArtistId;

-- 3) Faixas do gênero Rock
SELECT Track.Name AS TrackName, Album.Title AS AlbumName, Artist.Name AS ArtistName
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Genre.Name = 'Rock';

-- 4) Faixas longas
SELECT Track.Name AS TrackName, Track.Composer, Album.Title AS AlbumTitle
FROM Track
JOIN Album ON Track.AlbumId = Album.AlbumId
WHERE Track.Milliseconds > 300000;
