SELECT s.id, s.name, AVG(e.grade) AS avg_grade
FROM students AS s
JOIN evaluations AS e ON s.id = e.student_id
WHERE e.subject_id = ?  -- Здесь подставьте ID предмета
GROUP BY s.id, s.name
ORDER BY avg_grade DESC
LIMIT 1;