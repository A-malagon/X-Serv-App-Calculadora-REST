#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import socket


class CalculadoraRest(webapp.webApp):
    def tipoOperacion(self, operacion):
        if (len(self.operacion.split('+')) == 2):
            resultado = (float(self.operacion.split("+")[0]) +
                         float(self.operacion.split("+")[1]))
        elif (len(self.operacion.split('-')) == 2):
            resultado = (float(self.operacion.split("-")[0]) -
                         float(self.operacion.split("-")[1]))
        elif (len(self.operacion.split('x')) == 2):
            resultado = (float(self.operacion.split("x")[0]) *
                         float(self.operacion.split("x")[1]))
        elif (len(self.operacion.split('/')) == 2):
            resultado = (float(self.operacion.split("/")[0]) /
                         float(self.operacion.split("/")[1]))
        else:
            return ("Operacion incorrecta, introduce(+,-,/,x)")
        return resultado

    def parse(self, request):

        lista = request.split(" ", 2)
        cuerpo = request.split()[-1]
        metodo = lista[0]
        return(metodo, cuerpo)

    def process(self, parsedRequest):
        (metodo, cuerpo) = parsedRequest
        if (metodo == "PUT"):
            self.operacion = cuerpo
            return ("200 OK", "<html><body> La operacion es: "
                    + self.operacion + "</body></html>")
        elif (metodo == "GET"):
            try:
                resultado = self.tipoOperacion(self.operacion)
                return ("200 OK", "<html><body<El resultado es: " +
                        str(resultado) + "</body></html>")
            except AttributeError:
                return ("404 Not Found",
                        "<html><body>Operacion incorrecta</body></html>")
            except ValueError:
                return ("404 Not Found",
                        "<html><body>Operacion incorrecta</body></html>")
        else:
            return ("404 Not Found",
                    "<html><body>No es ni PUT ni GET</body></html>")

if __name__ == "__main__":
    MiCalculadora = CalculadoraRest(socket.gethostname(), 1234)
