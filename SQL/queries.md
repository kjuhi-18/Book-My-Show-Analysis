**Master queries**(

SELECT t.name AS theater\_name, AVG(s.price\_per\_ticket) AS avg\_ticket\_price

FROM Schedule sc

JOIN Shows s ON sc.show\_id = s.show\_id

JOIN Theaters t ON sc.theater\_id = t.theater\_id

GROUP BY t.theater\_id, t.name

HAVING AVG(s.price\_per\_ticket) > (

&nbsp;   SELECT AVG(price\_per\_ticket) FROM Shows

)

ORDER BY avg\_ticket\_price DESC

LIMIT 15;

SELECT \*

FROM (

&nbsp;   SELECT c.name, SUM(s.charges) AS total\_spent, COUNT(b.booking\_id) AS total\_bookings

&nbsp;   FROM c\_user c

&nbsp;   JOIN Reciepts r ON c.user\_id = r.user\_id

&nbsp;   JOIN Bookings b ON r.booking\_id = b.booking\_id

&nbsp;   JOIN Seats s ON b.booking\_id = s.booking\_id

&nbsp;   GROUP BY c.user\_id, c.name

&nbsp;   HAVING COUNT(b.booking\_id) > 1

&nbsp;   AND SUM(s.charges) > (

&nbsp;       SELECT AVG(total\_cost)

&nbsp;       FROM (

&nbsp;           SELECT SUM(charges) AS total\_cost

&nbsp;           FROM Seats

&nbsp;           GROUP BY booking\_id

&nbsp;       ) AS booking\_totals

&nbsp;   )

) AS temp

ORDER BY total\_spent DESC

LIMIT 15;)



**sub queries**(

SELECT title

FROM Movies

WHERE movie\_id IN (

&nbsp;   SELECT movie\_id

&nbsp;   FROM Reviews

&nbsp;   GROUP BY movie\_id

&nbsp;   HAVING AVG(rating) > (SELECT AVG(rating) FROM Reviews)

)

LIMIT 15;



SELECT c.name

FROM c\_user c

WHERE c.user\_id IN (

&nbsp;   SELECT r.user\_id

&nbsp;   FROM Reciepts r

&nbsp;   GROUP BY r.user\_id

&nbsp;   HAVING COUNT(r.booking\_id) > 1

)

LIMIT 15;)

**joins** 

(SELECT b.booking\_id, c.name, s.show\_date

FROM Bookings b

JOIN Reciepts r ON b.booking\_id = r.booking\_id

JOIN c\_user c ON r.user\_id = c.user\_id

JOIN Shows s ON r.show\_id = s.show\_id

LIMIT 15;

SELECT m.title, t.name AS theater\_name, sc.schedule\_id

FROM Schedule sc

JOIN Movies m ON sc.movie\_id = m.movie\_id

JOIN Theaters t ON sc.theater\_id = t.theater\_id

LIMIT 15;)

**Group by order by**(

SELECT r.user\_id, COUNT(b.booking\_id) AS total\_bookings

FROM Reciepts r

JOIN Bookings b ON r.booking\_id = b.booking\_id

GROUP BY r.user\_id

ORDER BY total\_bookings DESC

LIMIT 15;

Aggregate

SELECT m.title, AVG(rv.rating) AS avg\_rating

FROM Reviews rv

JOIN Movies m ON rv.movie\_id = m.movie\_id

GROUP BY m.title

ORDER BY avg\_rating DESC

LIMIT 15;

)

**aggregate**(

SELECT b.booking\_id, COUNT(s.seat\_id) AS seats\_booked

FROM Bookings b

JOIN Seats s ON b.booking\_id = s.booking\_id

GROUP BY b.booking\_id

LIMIT 15;



SELECT SUM(s.charges) AS total\_revenue

FROM Seats s;





