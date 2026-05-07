SELECT 
    s.name,
    e.per_pupil_expenditure,
    gr.graduated
FROM schools s
JOIN expenditures e
    ON s.district_id = e.district_id
JOIN graduation_rates gr
    ON s.id = gr.school_id
ORDER BY 
    per_pupil_expenditure DESC,
    name
;