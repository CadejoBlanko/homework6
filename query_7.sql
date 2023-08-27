SELECT s.name, e.grade
FROM students AS s
JOIN evaluations AS e ON s.id = e.student_id
WHERE s.groups_id = ? AND e.subject_id = ?;  -- Здесь подставьте ID группы и ID предмета
