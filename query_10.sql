SELECT s.subject_name
FROM student_subjects AS ss
JOIN subjects AS s ON ss.subject_id = s.id
WHERE ss.student_id = ? AND s.teacher_id = ?;  -- Здесь подставьте ID студента и ID преподавателя