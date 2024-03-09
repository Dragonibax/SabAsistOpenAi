gather_user_data = {
    "name": "gather_user_data",
    "description": "Obtener datos del usuario para agendar la cita en el hospital Bino",
    "parameters": {
        "type": "object",
        "properties": {
            "telefono": {"type": "string", "description": "Un telefono valido, e.g., 3362296959"},
            "nombre": {"type": "string", "description": "Primer nombre del usuario, e.g., David"},
            "apellido": {"type": "string", "description": "Apellido del usuario, e.g., Bustos"},
            "email": {"type": "string", "description": "Un email valido, e.g., david@gmail.com"},
        },
        "required": ["telefono", "nombre", "apellido", "email"]
    }
}

gather_reservation_data = {
    "name": "gather_reservation_data",
    "description": "Obtener los datos para agendar la cita en el hospital Bino",
    "parameters": {
        "type": "object",
        "properties": {
            "fecha": {"type": "string", "description": "Fecha deseada de visita, e.g., 2024-03-08"},
            "hora": {"type": "string", "description": "Hora deseada de visita, e.g., 4PM"}
        },
        "required": ["fecha", "hora"]
    }
}

gather_medical_reason = {
    "name": "gather_medical_reason",
    "description": "Obtener datos del del motivo de porque necesita una cita medica, sea una enfermedad un sintoma o un chequeo rutinario",
    "parameters": {
        "type": "object",
        "properties": {
            "razon": {"type": "string", "description": "Una causa para tener una cita medica, e.g., dolor estomacal"}
        },
        "required": ["razon"]
    }
}


not_talk = {
    "name": "not_talk",
    "description": "Preguntarle al usuario si quiere continuar hablando, si no desea terminar la ayuda del asistente",
    "parameters": {
        "type": "object",
        "properties": {
            "fin": {"type": "boolean", "description": "El usuario no quiere hablar mas"}
        },
        "required": ["fin"]
    }
}