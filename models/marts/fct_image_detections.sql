with detections as (
    select
        d.value ->> 'image' as image_file,
        d.value ->> 'class' as detected_object_class,
        (d.value ->> 'confidence')::float as confidence_score,
        d.value ->> 'timestamp' as detection_time
    from
        raw.telegram_image_detections,
        jsonb_array_elements(detection_data::jsonb) as d
)

select * from detections
