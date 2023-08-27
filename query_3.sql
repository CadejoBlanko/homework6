SELECT g.id, g.group_name, AVG(e.grade) AS avg_grade
FROM groups AS g
JOIN students AS s ON g.id = s.groups_id
JOIN evaluations AS e ON s.id = e.student_id
WHERE e.subject_id = ?  -- Здесь подставьте ID предмета
GROUP BY g.id, g.group_name;