SELECT s.subject_name
FROM subjects AS s
WHERE s.teacher_id = ?;  -- Здесь подставьте ID преподавателя