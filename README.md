# 🛡️ NmapReport Open

**NmapReport Open** es una herramienta para investigadores de seguridad y equipos Red Team que permite escanear **todos los puertos TCP** de un host y detectar rápidamente servicios expuestos, exportando los resultados a **Excel profesional**.

> ⚔️ Creado por Haak Cybersecurity Consulting — Seguridad que actúa, no solo advierte.

---

## 🎯 ¿Qué hace?

- Escanea los **65,535 puertos TCP** (`-p-`)
- Solo muestra puertos **abiertos** (`--open`)
- Usa opciones rápidas y silenciosas (`-Pn -T4 -n`)
- Detecta versiones de servicios (`-sV`)
- Exporta los resultados en un **.xlsx legible y listo para reportes**

---

## 🚀 Instalación

Requiere **Python 3.7+** y tener `nmap` instalado en tu sistema.

```bash
git clone https://github.com/tuusuario/nmapreport-open.git
cd nmapreport-open
pip install -r requirements.txt
```

---

## ⚙️ Uso

```bash
python3 nmapreport.py -t ejemplo.com -v -o reporte.xlsx
```

### Argumentos:

- `-t`, `--target`: IP o dominio a escanear
- `-o`, `--output`: Nombre del archivo Excel a generar (opcional)
- `-v`, `--verbose`: Activa modo detallado para ver el progreso

---

## 📌 Ejemplo de salida

```bash
[+] Ejecutando Nmap rápido contra ejemplo.com con -Pn -T4 -n -p- --open...
[+] Escaneo completado.
[+] Analizando resultados...
[+] Se encontraron 3 servicios.
[+] Reporte exportado exitosamente a: reporte.xlsx
```

---

## 💡 Casos de uso

- Auditorías de red internas o externas
- Reconocimiento en fases de pentest
- Automatización de reportes técnicos
- Análisis de superficie expuesta

---

## 👨‍💻 Autor

**Haak Cybersecurity Consulting**  
[https://haak.com.mx](https://haak.com.mx)

---

## ⚠️ Aviso legal

Este proyecto es solo para fines educativos y pruebas controladas.  
**No lo uses en infraestructuras sin autorización.**  
Haak Consulting no se responsabiliza por usos indebidos.

---

Made with 💻 by Alan Contreras - Haak Cybersecurity Consulting
