class VeracityController:
    @staticmethod
    def post():
        return {
            "status": "success",
            "message": "La noticia ha sido clasificada exitosamente.",
            "data": {
                "title": "Titulo de la noticia",
                "content": "Contenido de la noticia",
                "classification": True,
                "accuracy": 68,
            },
        }
