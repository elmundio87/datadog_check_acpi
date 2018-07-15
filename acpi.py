from checks import AgentCheck

class AcpiCheck(AgentCheck):

    METRIC_NAME_PREFIX = "acpi"

    def get_instance_config(self, instance):
        metric_name = instance.get('metric_name', None)
        metric_type = instance.get('metric_type', 'gauge')
        tags = instance.get('tags', [])

        if metric_name is None:
            raise Exception("A metric_name must be specified in the instance")

        if metric_type != "gauge" and metric_type != "rate":
            message = "Unsupported metric_type: {0}".format(metric_type)
            raise Exception(message)
 
        metric_name = "{0}.{1}".format(self.METRIC_NAME_PREFIX, metric_name)

        config = {
            "metric_name": metric_name,
            "metric_type": metric_type,
            "tags": tags
        }

        return config

    def check(self, instance):
        config = self.get_instance_config(instance)
        metric_name = config.get("metric_name")
        metric_type = config.get("metric_type")
        tags = config.get("tags")

	output = self.is_plugged()

        try:
            metric_value = float(output)
        except (TypeError, ValueError):
            raise Exception("Command must output a number.")

        if metric_type == "gauge":
            self.gauge(metric_name, metric_value, tags=tags)
        else:
            self.rate(metric_name, metric_value, tags=tags)

    def is_plugged(self):
        f=open('/sys/bus/acpi/drivers/ac/ACPI0003:00/power_supply/AC/online')
        res=f.read(1)
        f.close()
        return res

