-- 1) Clientes do Canadá
WITH ClientesCanada AS (
    SELECT FirstName, LastName, Email
    FROM Customer
    WHERE Country = 'Canada'
),

-- 2) Álbuns e Artistas
AlbunsArtistas AS (
    SELECT Album.Title AS AlbumName, Artist.Name AS ArtistName
    FROM Album
    JOIN Artist ON Album.ArtistId = Artist.ArtistId
),

-- 3) Faixas do gênero "Rock"
FaixasRock AS (
    SELECT Track.Name AS TrackName, Album.Title AS AlbumName, Artist.Name AS ArtistName
    FROM Track
    JOIN Genre ON Track.GenreId = Genre.GenreId
    JOIN Album ON Track.AlbumId = Album.AlbumId
    JOIN Artist ON Album.ArtistId = Artist.ArtistId
    WHERE Genre.Name = 'Rock'
),

-- 4) Faixas longas (maior que 300000 milissegundos)
FaixasLongas AS (
    SELECT Track.Name AS TrackName, Track.Composer, Album.Title AS AlbumTitle
    FROM Track
    JOIN Album ON Track.AlbumId = Album.AlbumId
    WHERE Track.Milliseconds > 300000
)

-- Exibindo os resultados de todas as CTEs
SELECT 
    'Clientes do Canadá' AS Categoria, 
    FirstName AS Nome, 
    LastName AS Sobrenome, 
    Email
FROM ClientesCanada

UNION ALL

SELECT 
    'Álbuns e Artistas', 
    AlbumName AS Nome, 
    ArtistName AS Sobrenome, 
    NULL AS Email
FROM AlbunsArtistas

UNION ALL

SELECT 
    'Faixas do Gênero Rock', 
    TrackName AS Nome, 
    ArtistName AS Sobrenome, 
    NULL AS Email
FROM FaixasRock

UNION ALL

SELECT 
    'Faixas Longas', 
    TrackName AS Nome, 
    Composer AS Sobrenome, 
    NULL AS Email
FROM FaixasLongas;
