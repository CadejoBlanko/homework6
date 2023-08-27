SELECT AVG(e.grade) AS avg_grade
FROM evaluations AS e
JOIN subjects AS s ON e.subject_id = s.id
WHERE s.teacher_id = ?;  -- Здесь подставьте ID преподавателя